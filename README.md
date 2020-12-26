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
3. 從`.env.sample`產生出一個`.env`，並填入以下四個資訊

- Line
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN
- Olami
    - APP_KEY
    - APP_SECRET
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
