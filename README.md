# TOC 台南即時天氣
## 構想
近年來各地天氣越來越不穩定，即使是舒適的台南，也越來越常出現突然降雨、降溫等的現象，因此能夠即時掌握天氣狀況來對天況做出應對，才不會一下子就著涼生病或是因為沒帶傘出門被淋成落湯雞，透過中央氣象局提供的即時數據，在經過統整後讓使用者能夠透過聊天機器人輕鬆查詢。
## 環境
- ubuntu 18.04
- python 3.6.9
## 使用教學
1. install `pipenv`
```shell
pip3 install pipenv
```
2. install 所需套件
```shell
pipenv install --three
// 若遇到pygraphviz安裝失敗，則嘗試下面這行
sudo apt-get install graphviz graphviz-dev
```
3. 以`.env.sample`的格式產生出一個`.env`，並填入以下資訊

- Line
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN
4. install `ngrok`

```shell
sudo snap install ngrok
```
5. run `ngrok` to deploy Line Chat Bot locally
```shell
ngrok http 8000
```
6. execute app.py
```shell
python3 app.py
```
## 使用步驟
1. 進入聊天室後按下任意鍵以開始，接著系統會要求輸入地名
2. 請輸入台南市中的行政區域+區(ex.`東區`、`中西區`)
3. 系統接著要求選擇服務種類，有`溫度`、`降雨機率`、`相對濕度`、以及`總體詳細情形`
4. 系統回傳結果
5. 在系統輸出結果之後，使用者可選擇重新選擇地點、服務或是離開聊天室
## FSM
![](https://raw.githubusercontent.com/C44051100/Line_Chat_Bot/main/img/fsm.png)
