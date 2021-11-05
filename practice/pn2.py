from asari.api import Sonar

list_text = [
    'この人は、この世の中で、いちばんしあわせな人にちがいありません。',
    '芝居小屋もすばらしいし、お客さんもすばらしい人たちでした。',
    'もし中世の時代だったら、おそらく、火あぶりにされたでしょうよ。',
    'みんなのうるさいことといったら、まるで、ハエがびんの中で、ブンブンいっているようでした。',
    'われわれ人間が、こういうことを考えだすことができるとすれば、われわれは、地の中にうめられるまでに、もっと長生きできてもいいはずだが'
]

# シンプルな動作確認
sonar = Sonar()
res = sonar.ping(text="広告多すぎる♡")
res
