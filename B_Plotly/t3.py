# 导入plotly包
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot,init_notebook_mode

# 使用离线模式的 plotly + cufflinks
import cufflinks
cufflinks.go_offline(connected=True)

# df['claps'].iplot(kind='hist', xTitle='claps', yTitle='count', title='Claps Distribution')
