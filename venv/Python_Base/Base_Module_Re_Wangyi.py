# _*_  encoding:utf-8  _*_
''''
目标：学习python正则表达式获取数据,爬取网易部分歌曲名称S
时间：2020年03月28日
作者：Miss Fu
'''
#导入模块
from lxml import etree


#定义爬取内容后测试正则表达式是否正确
conment = '''
<dl class="blk ">
<dt class="top">
<div class="cver u-cover u-cover-4">
<img class="j-img" data-src="http://p4.music.126.net/DrRIg6CrgDfVLEph9SNh7w==/18696095720518497.jpg?param=100y100" src="http://p4.music.126.net/DrRIg6CrgDfVLEph9SNh7w==/18696095720518497.jpg?param=100y100">
<a href="/discover/toplist?id=19723756" class="msk" title="云音乐飙升榜"></a>
</div>
<div class="tit">
<a href="/discover/toplist?id=19723756" title="云音乐飙升榜"><h3 class="f-fs1 f-thide">云音乐飙升榜</h3></a>
<div class="btn">
<a href="javascript:;" class="s-bg s-bg-9 f-tdn" hidefocus="true" title="播放" data-res-type="13" data-res-id="19723756" data-res-action="play" data-res-from="31" data-res-data="19723756">播放</a>
<a href="javascript:;" hidefocus="true" class="s-bg s-bg-10 f-tdn subscribe-flag " data-plid="19723756" title="收藏">收藏</a>
</div>
</div>
</dt>
<dd>
<ol>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''" class="">
<span class="no no-top">1</span>
<a href="/song?id=1433984099" class="nm s-fc0 f-thide" title="有一件美好的事情将要发生">有一件美好的事情将要发生</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1433984099" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1433984099" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1433984099" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''" class="">
<span class="no no-top">2</span>
<a href="/song?id=1434062381" class="nm s-fc0 f-thide" title="达拉崩吧 (Live)">达拉崩吧 (Live)</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1434062381" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1434062381" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1434062381" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''" class="">
<span class="no no-top">3</span>
<a href="/song?id=1387581250" class="nm s-fc0 f-thide" title="MOM">MOM</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1387581250" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1387581250" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1387581250" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''" class="z-hvr">
<span class="no">4</span>
<a href="/song?id=1434057772" class="nm s-fc0 f-thide" title="新世界 (Live)">新世界 (Live)</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1434057772" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1434057772" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1434057772" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''" class="">
<span class="no">5</span>
<a href="/song?id=1427912360" class="nm s-fc0 f-thide" title="冰天雪地">冰天雪地</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1427912360" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1427912360" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1427912360" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''" class="">
<span class="no">6</span>
<a href="/song?id=1432427879" class="nm s-fc0 f-thide" title="有可能的夜晚 (Live)">有可能的夜晚 (Live)</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1432427879" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1432427879" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1432427879" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''" class="">
<span class="no">7</span>
<a href="/song?id=1426233208" class="nm s-fc0 f-thide" title="痛快">痛快</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1426233208" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1426233208" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1426233208" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''" class="">
<span class="no">8</span>
<a href="/song?id=1434201430" class="nm s-fc0 f-thide" title="BELIEVE IT">BELIEVE IT</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1434201430" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1434201430" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1434201430" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''">
<span class="no">9</span>
<a href="/song?id=1434057755" class="nm s-fc0 f-thide" title="半途而废 (Live)">半途而废 (Live)</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1434057755" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1434057755" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1434057755" data-res-action="subscribe"></a>
</div>
</li>
<li onmouseover="this.className='z-hvr'" onmouseout="this.className=''">
<span class="no">10</span>
<a href="/song?id=1426649237" class="nm s-fc0 f-thide" title="海底">海底</a>
<div class="oper">
<a href="#" class="s-bg s-bg-11" title="播放" hidefocus="true" data-res-type="18" data-res-id="1426649237" data-res-action="play" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="u-icn u-icn-81" title="添加到播放列表" hidefocus="true" data-res-type="18" data-res-id="1426649237" data-res-action="addto" data-res-from="31" data-res-data="19723756"></a>
<a href="#" class="s-bg s-bg-12" title="收藏" hidefocus="true" data-res-level="0" data-res-fee="8" data-res-type="18" data-res-id="1426649237" data-res-action="subscribe"></a>
</div>
</li>
</ol>
<div class="more"><a href="/discover/toplist?id=19723756" class="s-fc0">查看全部&gt;</a></div>
</dd>
</dl>
'''
# result = re.findall('</li.*?">.*?<span.*?">(.*?)</span>.*?href="(.*?)".*?">(.*?)</a>',conment,re.S)
#
# for totul in result:
#      print(totul)

# for results in result:
#     number,url,name = results
#     url = re.sub(url)
#     name = re.sub(name)
#     print(number,url,name)

#通过xpath方法来获取数据
result = etree.HTML(conment)
wl_data = result.xpath('//li/a//@href|//li/a//@title')
print(wl_data)


