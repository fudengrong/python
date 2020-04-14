
from lxml import etree
wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """
# html = etree.HTML(wb_data)
# print(html)

#补全不完整HTML代码
# html_Format = etree.tostring(html)
# print(html_Format.decode('utf-8'))

#获取a标签的所有内容
html = etree.HTML(wb_data)
html_Data = html.xpath('/html/body/div/ul/li/a/text()')
print(html)
for i in html_Data:
    print(i.text)

