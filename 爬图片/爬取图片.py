import requests
import parsel

for page in range(1, 5):
    url = f"https://www.kanxiaojiejie.com/page/{page}"
    response = requests.get(url)
    HTML_data = response.text
    # print(response.text)
    selector = parsel.Selector(HTML_data)
    link_url = selector.css(".entry-title a::attr(href)").getall()
    # print(link_url)
    for link in link_url:
        response_1 = requests.get(link)
        # print(response_1.text)
        html_data_1 = response_1.text
        selector_1 = parsel.Selector(html_data_1)
        img_list = selector_1.css(".entry.themeform p img::attr(src)").getall()
        # print(img_list)
        for img in img_list:
            img_name = img.split('/')[-1]
            img_data = requests.get(img).content
            with open(f'img/{img_name}', mode='wb') as f:
                f.write(img_data)
            print("正在爬取： ", img_name)
print("爬取成功")
