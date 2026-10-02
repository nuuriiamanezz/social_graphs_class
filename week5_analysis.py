# Week 5 post: in-degree vs page length and Heaps law. Run from the repo root after unzipping data_5/marvel_pages.zip into data_5/marvel_pages/.
import re, glob, os, urllib.parse, numpy as np, pandas as pd, networkx as nx
from collections import Counter
U='.'
nodes=pd.read_csv(U+'/data_1/week1_nodes.tsv',sep='\t',comment='#')
edges=pd.read_csv(U+'/data_1/week1_edges.tsv',sep='\t',comment='#',names=['source','target'])
edges=edges[edges.source!='source']
G=nx.DiGraph(); G.add_nodes_from(nodes.node_id); G.add_edges_from(zip(edges.source,edges.target))
texts={}
for f in glob.glob('data_5/marvel_pages/marvel_pages/*.txt'):
    s=os.path.basename(f)[:-4]
    if s=='README': continue
    texts[urllib.parse.unquote(s)]=open(f,encoding='utf-8').read()
TOK=re.compile(r"[a-z0-9]+(?:['’\-][a-z0-9]+)*")
def tok(t): return TOK.findall(t.lower())
toks={k:tok(v) for k,v in texts.items()}
df=pd.DataFrame({'node':list(texts)})
df['indeg']=[G.in_degree(n) for n in df.node]; df['outdeg']=[G.out_degree(n) for n in df.node]
df['chars']=[len(texts[n]) for n in df.node]
df['tokens']=[len(toks[n]) for n in df.node]; df['types']=[len(set(toks[n])) for n in df.node]
from scipy import stats
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
BG='#120014'; PINK='#ff2e9c'; CY='#00e5ff'; YE='#ffe14d'; TX='#fdf1fb'; DIM='#cba8c9'; GR='#3a1f3f'
plt.rcParams.update({'figure.facecolor':BG,'axes.facecolor':BG,'savefig.facecolor':BG,'text.color':TX,'axes.labelcolor':TX,'xtick.color':DIM,'ytick.color':DIM,'axes.edgecolor':'#4a2450','font.size':12})
fig,(a1,a2)=plt.subplots(1,2,figsize=(14,6.4),dpi=130)
fam=df.indeg>=8
rng=np.random.default_rng(1); jit=10**rng.uniform(-0.035,0.035,len(df))
x=(df.indeg+1)*jit
a1.scatter(x[~fam],df.tokens[~fam],s=22,c=CY,alpha=.65,lw=0,label=f'in-degree 0–7 (n={int((~fam).sum())})')
a1.scatter(x[fam],df.tokens[fam],s=26,c=PINK,alpha=.8,lw=0,label=f'in-degree 8+ (n={int(fam.sum())})')
s,i=np.polyfit(np.log10(df.indeg+1),np.log10(df.tokens),1); xx=np.array([1,110]); a1.plot(xx,10**i*xx**s,'--',c=YE,lw=1.6)
rho=stats.spearmanr(df.indeg,df.tokens)[0]
a1.set(xscale='log',yscale='log',xlabel='in-degree + 1  (pages in the category linking here)',ylabel='page length (tokens)')
a1.set_title(f'Fame buys length  (Spearman ρ = {rho:.2f})',color=TX,pad=10)
lab={'Spider-Man':(1.0,0.45),'Quasar_(character)':(1.05,0.62),'Betsy_Braddock':(0.42,1.2),'Scarlet_Witch':(0.9,1.22),'Helix_(Marvel_Comics)':(1.15,0.92),'Hulk':(0.6,0.55)}
for n,(dx,dy) in lab.items():
    r=df[df.node==n].iloc[0]; a1.annotate(n.split('_(')[0].replace('_',' '),(r.indeg+1,r.tokens),xytext=((r.indeg+1)*dx,r.tokens*dy),color=DIM,fontsize=10,ha=('right' if n=='Spider-Man' else 'left'),arrowprops=dict(arrowstyle='-',color=DIM,lw=.6))
a1.legend(frameon=False,loc='lower right',fontsize=10)
lt=np.log10(df.tokens); b,a,r,_,_=stats.linregress(lt,np.log10(df.types))
a2.scatter(df.tokens[~fam],df.types[~fam],s=22,c=CY,alpha=.65,lw=0); a2.scatter(df.tokens[fam],df.types[fam],s=26,c=PINK,alpha=.8,lw=0)
xx=np.array([170,16000]); a2.plot(xx,10**a*xx**b,'--',c=YE,lw=1.6,label=f'Heaps fit: V = {10**a:.1f}·N^{b:.2f}  (R² = {r*r:.3f})'); a2.plot(xx,xx,':',c=DIM,lw=1,label='V = N (every token a new word)')
a2.set(xscale='log',yscale='log',xlabel='page length N (tokens)',ylabel='vocabulary V (distinct types)',ylim=(90,6000))
a2.set_title('…but not a richer vocabulary: one Heaps curve fits all',color=TX,pad=10); a2.legend(frameon=False,loc='upper left',fontsize=10)
for ax in (a1,a2): ax.grid(True,which='major',color=GR,lw=.5,alpha=.6)
fig.tight_layout(); fig.savefig('assets/img/fig_fame_vs_words.png'); print(rho,s,b,10**a,r*r,fam.sum())
