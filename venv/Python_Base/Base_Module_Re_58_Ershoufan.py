# _*_  encoding:utf-8  _*_
''''
目标：学习python正则表达式获取数据,爬取58同城二手房信息
时间：2020年03月28日
作者：Miss Fu
'''
#导入模块
import re
import requests
from lxml import etree
conment = '''
<li logr="gz_1_56617347735321_41527594665734" _pos="1" class="sendsoj" data-trace="{
                                                                                                                esf_id:41527594665734,
                            isauction:200,
                            pos:1,source_type:3,
                            entity_id: &quot;1393490432793614&quot;,
                            tid: &quot;eb6328db-d19c-4463-902f-b62c8cad9358&quot;
                                                    }">
                        <div class="pic">
                            <a href="https://cq.58.com/ershoufang/41527594665734x.shtml?utm_source=market&amp;spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&amp;cityListName=cq&amp;curListName=bnlijiatuo&amp;lg=https%3A%2F%2Flegoclick.58.com%2Fjump%3Ftarget%3DszqW0i3draOWUvYfugF1pAqduh78uztYnHNzP1NOPjmvPH01PZ980v6YUykKuadbuyu-PvNzuBYvuywbsHELmynVryDdmidhPjPbPvPBuAPbrH9KPHmvnH01Pj0Ln1N1nWDKTHD1rHnYrHTYn1cLrHnvnHEKnHbknjTKnHbknjTKnikQnkDQnjm_nHTvPzkQnWcdrTDQPH9dn19YPWnkPj9QTHDKwbnVNDnVOsJnOChsOCB4OsBeOmBgl2AClpAdTHDKnE7hmdqkmvYQn-q8UvO-xjD_ugF1pAqduh78udqCug-6U-q-XZKx0APVxjDKsHDKTHDzPjnLn10YnWTOnHNkn1mQPWTKP9DKnEDkmhEdryuhmidBPAmdsHEzmWcVrH9YPaYYmh76PH-hmH76ryEKnHcYn101P1EznHTdn1EYrjDOn9DQnWE1P1nLPjckrHbkPHn1PWnzTEDKTHE8rjmQnHmvwiYdTEDVTyd60hV-IT7dsHFbnM-3IW9vXHPvPjP8pvwbpjD8EbwEEdKpgYFNTy6YIZK1rBtfmLD8PH98mvqVsvF8UA-Jpy7YIytfugF1pAqduh78uzt4IgwVgLPfIgFWuHdVmgFougEh0LKV5gNVnhEzXg6vrjuOnLmYnvOouAwCniOaw7KjN7GxE-EKwgG7uD_QPyqm0AnfrRum0durXgurI1YqTHDzPi33Pi3zn1c8nHD3THTKnTDKnikQnk7exEDQnjT1n9DQnjTQPj9LTyRBPWnzrAwBsyEQrynVPjEvnzYOnjFhsycvnhn3mv7brHndrTDKnTDKTHTKnHTvsjDkPW0_nHczPH9Kn9DznHnzPjRbPWP6rHPBmWKb&amp;psid=ce279c13-02a4-4a46-9ad7-6c1beff06b7e&amp;entinfo=41527594665734_0&amp;fzbref=0&amp;key=&amp;referinfo=FALSE&amp;typecode=200&amp;from=1-list-0" target="_blank">
                                <img alt="" src="https://pic1.ajkimg.com/display/58ajk/c156b28abd8dc338a2057622a9a6afc5/500x500.jpg?w=480&amp;h=360&amp;crop=1" style="display: inline;">
                                                                    <i class="VRIcon"></i>
                                    <i class="videoIcon bothIcon"></i>
                                                            </a>
                                                        <span class="picNum">14图</span>
                                                    </div>
                        <div class="list-info">
                            <h2 class="title">
                                <a href="https://cq.58.com/ershoufang/41527594665734x.shtml?utm_source=market&amp;spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&amp;cityListName=cq&amp;curListName=bnlijiatuo&amp;lg=https%3A%2F%2Flegoclick.58.com%2Fjump%3Ftarget%3DszqW0i3draOWUvYfugF1pAqduh78uztYnHNzP1NOPjmvPH01PZ980v6YUykKuadbuyu-PvNzuBYvuywbsHELmynVryDdmidhPjPbPvPBuAPbrH9KPHmvnH01Pj0Ln1N1nWDKTHD1rHnYrHTYn1cLrHnvnHEKnHbknjTKnHbknjTKnikQnkDQnjm_nHTvPzkQnWcdrTDQPH9dn19YPWnkPj9QTHDKwbnVNDnVOsJnOChsOCB4OsBeOmBgl2AClpAdTHDKnE7hmdqkmvYQn-q8UvO-xjD_ugF1pAqduh78udqCug-6U-q-XZKx0APVxjDKsHDKTHDzPjnLn10YnWTOnHNkn1mQPWTKP9DKnEDkmhEdryuhmidBPAmdsHEzmWcVrH9YPaYYmh76PH-hmH76ryEKnHcYn101P1EznHTdn1EYrjDOn9DQnWE1P1nLPjckrHbkPHn1PWnzTEDKTHE8rjmQnHmvwiYdTEDVTyd60hV-IT7dsHFbnM-3IW9vXHPvPjP8pvwbpjD8EbwEEdKpgYFNTy6YIZK1rBtfmLD8PH98mvqVsvF8UA-Jpy7YIytfugF1pAqduh78uzt4IgwVgLPfIgFWuHdVmgFougEh0LKV5gNVnhEzXg6vrjuOnLmYnvOouAwCniOaw7KjN7GxE-EKwgG7uD_QPyqm0AnfrRum0durXgurI1YqTHDzPi33Pi3zn1c8nHD3THTKnTDKnikQnk7exEDQnjT1n9DQnjTQPj9LTyRBPWnzrAwBsyEQrynVPjEvnzYOnjFhsycvnhn3mv7brHndrTDKnTDKTHTKnHTvsjDkPW0_nHczPH9Kn9DznHnzPjRbPWP6rHPBmWKb&amp;psid=ce279c13-02a4-4a46-9ad7-6c1beff06b7e&amp;entinfo=41527594665734_0&amp;fzbref=0&amp;key=&amp;referinfo=FALSE&amp;typecode=200&amp;from=1-list-0&amp;iuType=gz_1&amp;PGTID=0d30000c-0302-8c3e-b5b2-bba0a1f281aa&amp;ClickID=1" tongji_label="listclick" target="_blank" onclick="clickLog('from=fcpc_ersflist_gzcount');">李家沱，斌鑫江南御府精装3房2卫，真材实料价格1&nbsp;</a>
                                                                                                    <i class="icon-container">
                                                                                    <i class="icon icon-jinpai" title="精选房源">精</i>
                                                                                                                                                                            <i class="icon icon-anxuan-all">
                                                    <i class="icon-anxuan-icon"></i>
                                                    <i class="icon-anxuan-text">真实在售</i>
                                                </i>
                                                                                                                        </i>
                                                            </h2>
                            <p class="baseinfo">
                                <span>3室2厅2卫</span>
                                <span>92.13㎡&nbsp;</span>
                                <span>东南</span>
                                <span>中层(共33层)</span>
                            </p>
                            <p class="baseinfo">

                                    <span>
                                                                                    <a href="/xiaoqu/binxinjiangnanyufu/ershoufang/" target="_blank">斌鑫江南御府</a>

                                         -                                                                                     <a href="/banan/ershoufang/" target="_blank">巴南</a>
                                                                                 -                                                                                     <a>龙洲大道1788号</a>
                                                                            </span>

                                                                    <span><i class="icon dtIcon"></i>距离3号线花溪地铁站1012米</span>
                                                            </p>
                            <div class="jjrinfo">
                                                                                                                                                                        <span class="anxuan-qiye-text">广西优居科技有限公司</span>
                                                                                                                <span class="anxuan-qiye-text">-</span>
                                                                                                            <a href="javascript:;" class="listjjr anxuan-qiye-text">
                                        <span class="jjrname-outer">何友兴</span>
                                        <div class="jjrtip">
                                            <img src="https://img.58cdn.com.cn/ui9/house/list/list_jjr.png" alt="经纪人图像" class="logo">
                                            <p class="jjrName">
                                                <span class="jjrName_span">何友兴</span>
                                                <span class="wlt"> <em class="wltico"></em>年 </span>
                                            </p>
                                            <p class="jjrrenz">  优居优住<br>  58同城认证商家
                                            </p>
                                            <span class="tipArrow"></span>
                                        </div>
                                    </a>
                                        <!-- 经纪人角色模块 -->
                                                                                                                                                                        </div>
                        </div>
                        <div class="price">
                            <p class="sum"><b>108</b>万</p>
                            <p class="unit">11723元/㎡</p>
                        </div>
                                                    <div class="time guanggao">广告</div>
                                            </li>
'''

# url = 'https://cq.58.com/bnlijiatuo/ershoufang/?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d30000c-0149-162c-6b87-0aabca2e449c&ClickID=1'
# conment = requests.get(url).text
#Ershoufan = re.findall('<li.*?<div.*?">.*?href="(.*?)".*">(.*?)</a>.*?baseinfo.*?<span>(.*?)</span>.*?baseinfo.*?target="(.*?)".*?price.*?class="(.*?)".*?</li>',conment,re.S)


# Ershoufan = re.findall('<li.*?list-info.*?">(.*?)</a>.*?baseinfo.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?<span>(.*?)</span>.*?price.*?<b>(.*?)</p>.*?">(.*?)</p>.*?</li>',conment,re.S)


