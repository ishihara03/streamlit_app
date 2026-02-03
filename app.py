import streamlit as st
import pandas as pd
import plotly.express as px

#品目,年度,国内生産量【1000トン】,外国貿易_輸入量【1000トン】,外国貿易_輸出量【1000トン】,在庫の増減量【1000トン】,国内消費仕向量【1000トン】,国内消費仕向量の内訳_飼料用【1000トン】,国内消費仕向量の内訳_種子用【1000トン】,国内消費仕向量の内訳_加工用【1000トン】,国内消費仕向量の内訳_純旅客用【1000トン】,国内消費仕向量の内訳_減耗量【1000トン】,国内消費仕向量の内訳_粗食料_総数【1000トン】,国内消費仕向量の内訳_粗食料_１人１年当たり【kg】,国内消費仕向量の内訳_粗食料_１人１日当たり【ｇ】,国内消費仕向量の内訳_歩留り【％】,国内消費仕向量の内訳_純食料【1000トン】,１人当たり供給純食料_１年当たり数量【kg】,１人当たり供給純食料_１日当たり_数量【ｇ】,１人当たり供給純食料_１日当たり_熱量【kcal】,１人当たり供給純食料_１日当たり_たんぱく質【ｇ】,１人当たり供給純食料_１日当たり_脂質【ｇ】,純食料100g中の栄養成分量_熱量【kcal】,純食料100g中の栄養成分量_たんぱく質【ｇ】,純食料100g中の栄養成分量_脂質【ｇ】
#国内消費志向量の内訳_飼料用【1000トン】の内訳以降のデータは使用しない
#csv区切りの,以外は削除
df = pd.read_csv('00500300-66-20250314.csv', encoding='cp932', thousands=',')
df = df.iloc[:, :7]

st.title('食料需給データ分析')
st.caption("2026/02/03更新")

df['食料自給率（%）'] = (df['国内生産量【1000トン】'] / df['国内消費仕向量【1000トン】'] *100)

popover = st.popover("表示するデータを選択してください")
selected1 = popover.checkbox('食料総取得量', value=True)
selected2 = popover.checkbox('食料総消費量', value=True)
selected3 = popover.checkbox('食料自給率', value=True)
selected4 = popover.checkbox('全データの表', value=False)

#グラフ描画（チェックボックスの入力で表示を切り替え）
if selected1:
  fig = px.bar(df, x='年度', y=['国内生産量【1000トン】', '外国貿易_輸入量【1000トン】'], title='日本の食料総取得量')
  st.plotly_chart(fig)
if selected2:
  fig = px.bar(df, x='年度', y=['国内消費仕向量【1000トン】', '外国貿易_輸出量【1000トン】'], title='日本の食料総消費量')
  st.plotly_chart(fig)
if selected3:  
  fig = px.line(df, x='年度', y='食料自給率（%）', title='日本の食料自給率（%）')
  st.plotly_chart(fig)

#使用したデータの表示
if selected4:
  st.dataframe(df)
  with st.expander('使用したデータ'):
    st.write('食料需給表 食料需給表 / 確報 / 令和５年度食料需給表 調査年月  2023年度 公開（更新）日  2025-03-14')
    st.write('https://www.e-stat.go.jp/stat-search?page=1&query=%E9%A3%9F%E6%96%99%E8%87%AA%E7%B5%A6%E7%8E%87&layout=dataset&toukei=00500300&bunya_l=04&metadata=1&data=1')
