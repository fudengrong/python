# _*_  encoding:utf-8  _*_
import re

html = '''
<div class="rank-list-box" data-v-53224597=""><div class="rank-list-item pr"><span class="num less-three-num">
            01
            </span><a href="/song/674842469" title="歌曲-Silent Night-Japanese ver.-" target="_blank" class=""><img data-src="http://qukufile2.qianqian.com/data2/pic/7fc3a44e71b247aa83efc9f2664d4794/674842488/674842488.jpg@s_2,w_60,h_60" src="http://qukufile2.qianqian.com/data2/pic/7fc3a44e71b247aa83efc9f2664d4794/674842488/674842488.jpg@s_2,w_60,h_60" title="歌曲-Silent Night-Japanese ver.-" alt="Silent Night-Japanese ver.-" class="pic" lazy="loaded"></a><div class="info"><h3 class="to"><a href="/song/674842469" title="歌曲-Silent Night-Japanese ver.-" target="_blank" class="song-title t">Silent Night-Japanese ver.-
                    </a></h3><h4 data-ss="Dreamcatcher" data-aa="2517688" class="to"><a href="/artist/35609" title="歌手-Dreamcatcher" target="_blank" class="song-name">Dreamcatcher
                    </a></h4></div><div class="tool-bar" data-v-2113e2c9=""><i data-type="play" class="t iconfont icon-hover_play" data-v-2113e2c9=""></i><i data-type="add" class="t iconfont icon-hover_add" data-v-2113e2c9=""></i><i data-type="download" class="t iconfont icon-hover_download" data-v-2113e2c9=""></i><!----></div></div><div class="rank-list-item pr"><span class="num less-three-num">
            02
            </span><a href="/song/674859467" title="歌曲-小情歌（Little Love Song）" target="_blank" class=""><img data-src="http://qukufile2.qianqian.com/data2/pic/28f7f891ca772b61988637bbc17cad53/674859474/674859474.jpg@s_2,w_60,h_60" src="http://qukufile2.qianqian.com/data2/pic/28f7f891ca772b61988637bbc17cad53/674859474/674859474.jpg@s_2,w_60,h_60" title="歌曲-小情歌（Little Love Song）" alt="小情歌（Little Love Song）" class="pic" lazy="loaded"></a><div class="info"><h3 class="to"><a href="/song/674859467" title="歌曲-小情歌（Little Love Song）" target="_blank" class="song-title t">小情歌（Little Love Song）
                    </a></h3><h4 data-ss="MiniG迷你机" data-aa="612873800" class="to"><a href="/artist/340506688" title="歌手-MiniG迷你机" target="_blank" class="song-name">MiniG迷你机
                    </a></h4></div><div class="tool-bar" data-v-2113e2c9=""><i data-type="play" class="t iconfont icon-hover_play" data-v-2113e2c9=""></i><i data-type="add" class="t iconfont icon-hover_add" data-v-2113e2c9=""></i><i data-type="download" class="t iconfont icon-hover_download" data-v-2113e2c9=""></i><!----></div></div><div class="rank-list-item pr"><span class="num less-three-num">
            03
            </span><a href="/song/674842468" title="歌曲-Over the Sky-Japanese ver.-" target="_blank" class=""><img data-src="http://qukufile2.qianqian.com/data2/pic/7fc3a44e71b247aa83efc9f2664d4794/674842488/674842488.jpg@s_2,w_60,h_60" src="http://qukufile2.qianqian.com/data2/pic/7fc3a44e71b247aa83efc9f2664d4794/674842488/674842488.jpg@s_2,w_60,h_60" title="歌曲-Over the Sky-Japanese ver.-" alt="Over the Sky-Japanese ver.-" class="pic" lazy="loaded"></a><div class="info"><h3 class="to"><a href="/song/674842468" title="歌曲-Over the Sky-Japanese ver.-" target="_blank" class="song-title t">Over the Sky-Japanese ver.-
                    </a></h3><h4 data-ss="Dreamcatcher" data-aa="2517688" class="to"><a href="/artist/35609" title="歌手-Dreamcatcher" target="_blank" class="song-name">Dreamcatcher
                    </a></h4></div><div class="tool-bar" data-v-2113e2c9=""><i data-type="play" class="t iconfont icon-hover_play" data-v-2113e2c9=""></i><i data-type="add" class="t iconfont icon-hover_add" data-v-2113e2c9=""></i><i data-type="download" class="t iconfont icon-hover_download" data-v-2113e2c9=""></i><!----></div></div><div class="rank-list-item pr"><span class="num">
            04
            </span><a href="/song/674842467" title="歌曲-Endless Night" target="_blank" class=""><img data-src="http://qukufile2.qianqian.com/data2/pic/7fc3a44e71b247aa83efc9f2664d4794/674842488/674842488.jpg@s_2,w_60,h_60" src="http://qukufile2.qianqian.com/data2/pic/7fc3a44e71b247aa83efc9f2664d4794/674842488/674842488.jpg@s_2,w_60,h_60" title="歌曲-Endless Night" alt="Endless Night" class="pic" lazy="loaded"></a><div class="info"><h3 class="to"><a href="/song/674842467" title="歌曲-Endless Night" target="_blank" class="song-title t">Endless Night
                    </a></h3><h4 data-ss="Dreamcatcher" data-aa="2517688" class="to"><a href="/artist/35609" title="歌手-Dreamcatcher" target="_blank" class="song-name">Dreamcatcher
                    </a></h4></div><div class="tool-bar" data-v-2113e2c9=""><i data-type="play" class="t iconfont icon-hover_play" data-v-2113e2c9=""></i><i data-type="add" class="t iconfont icon-hover_add" data-v-2113e2c9=""></i><i data-type="download" class="t iconfont icon-hover_download" data-v-2113e2c9=""></i><!----></div></div><div class="rank-list-item pr"><span class="num">
            05
            </span><a href="/song/674728859" title="歌曲-光的摩斯密码（电视剧《你好检察官》插曲）" target="_blank" class=""><img data-src="http://qukufile2.qianqian.com/data2/pic/e34895c1cf42e18a27b1c590693f76cd/674766269/674766269.jpg@s_2,w_60,h_60" src="http://qukufile2.qianqian.com/data2/pic/e34895c1cf42e18a27b1c590693f76cd/674766269/674766269.jpg@s_2,w_60,h_60" title="歌曲-光的摩斯密码（电视剧《你好检察官》插曲）" alt="光的摩斯密码（电视剧《你好检察官》插曲）" class="pic" lazy="loaded"></a><div class="info"><h3 class="to"><a href="/song/674728859" title="歌曲-光的摩斯密码（电视剧《你好检察官》插曲）" target="_blank" class="song-title t">光的摩斯密码（电视剧《你好检察官》插曲）
                    </a></h3><h4 data-ss="刘惜君" data-aa="1665" class="to"><a href="/artist/2611" title="歌手-刘惜君" target="_blank" class="song-name">刘惜君
                    </a></h4></div><div class="tool-bar" data-v-2113e2c9=""><i data-type="play" class="t iconfont icon-hover_play" data-v-2113e2c9=""></i><i data-type="add" class="t iconfont icon-hover_add" data-v-2113e2c9=""></i><i data-type="download" class="t iconfont icon-hover_download" data-v-2113e2c9=""></i><!----></div></div><div class="rank-list-item pr"><span class="num">
            06
            </span><a href="/song/674658149" title="歌曲-情非得已" target="_blank" class=""><img data-src="http://qukufile2.qianqian.com/data2/pic/fd9bcd2ce6c41f372b1cda42d1c3f67b/674658192/674658192.jpg@s_2,w_60,h_60" src="http://qukufile2.qianqian.com/data2/pic/fd9bcd2ce6c41f372b1cda42d1c3f67b/674658192/674658192.jpg@s_2,w_60,h_60" title="歌曲-情非得已" alt="情非得已" class="pic" lazy="loaded"></a><div class="info"><h3 class="to"><a href="/song/674658149" title="歌曲-情非得已" target="_blank" class="song-title t">情非得已
                    </a></h3><h4 data-ss="曾惜" data-aa="238665373" class="to"><a href="/artist/209854097" title="歌手-曾惜" target="_blank" class="song-name">曾惜
                    </a></h4></div><div class="tool-bar" data-v-2113e2c9=""><i data-type="play" class="t iconfont icon-hover_play" data-v-2113e2c9=""></i><i data-type="add" class="t iconfont icon-hover_add" data-v-2113e2c9=""></i><i data-type="download" class="t iconfont icon-hover_download" data-v-2113e2c9=""></i><!----></div></div></div>
'''
  



#result = re.match('^<a\shref="(/\/w\/d(.*?))"\s$title',html,re.S)

#result = re.search('<a.*?href="(/\/w\/d(.*?))".*?title="(.*?)".*?$/a>',html)
result = re.findall('<a.*?href="(.*?)".*?title="(.*?)".*?\s',html,re.S)
#print(result)
for results in result:
    print(results[0],results[1])


