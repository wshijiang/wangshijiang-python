import dns.resolver

def dns_query(domain, dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]

    while True:
        try:
            # 发送查询
            response_a = resolver.resolve(domain, 'A')
            response_aaaa = resolver.resolve(domain, 'AAAA')
            response_cname = resolver.resolve(domain, 'CNAME')

            # 输出Ａ记录回复
            print('A记录查询回复：')
            for answer in response_a:
                print(f'{domain} 的IPv4地址是：{answer.address}')
                print(f"返回数据大小为： {len(response_a.response.to_wire())} bytes")

            # 输出AAAA记录回复
            print('AAAA记录查询回复：')
            for answer in response_aaaa:
                print(f'{domain} 的IPv6地址是：{answer.address}')
                print(f"返回数据大小为： {len(response_aaaa.response.to_wire())} bytes")

            # 输出CNAME记录回复
            print('CNAME记录查询回复：')
            for answer in response_cname:
                print(f'{domain} 的CNAME记录是：{answer.target}')
                print(f"返回数据大小为： {len(response_cname.response.to_wire())} bytes")
            break
        except dns.exception.DNSException as e:
            print(f'DNS查询失败：{e}')
            print(f"请跟换域名{e}或DNS再次进行查询")
            break

print("域名查询-Python(3.11.4)\n作者：wangshijiang\n"
      "GitHub: https://github.com/iwqculrbud/wangshijiang-python.git\n"
      "QQ: 3145865693")
while True:
    dns_query(domain=input("输入查询的域名（建议为xx.com格式）: "),
              dns_server=input("输入DNS服务器（建议为114.114.114.114）:"
                               ))
    while True:
        decide = input("您还要继续吗？（y/n）: ")
        if decide.lower() == 'n':
            exit(1)
        elif decide.lower() == 'y':
            print("谢谢您的支持!!!")
            break
        else:
            print(f"您输入的　{decide}　不合规，只有y/n（不分大小写）。")
