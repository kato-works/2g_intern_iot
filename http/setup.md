# Raspberry Pi をサーバとしてセットアップする

## Wi-Fiアクセスポイントに変更

### Raspberry Piを最新の状態に更新し、必要なパッケージをインストール

```sh
sudo apt update
sudo apt upgrade
sudo apt install hostapd dnsmasq
```

- hostapd : ネットワークインターフェイスカードがアクセスポイントおよび認証サーバーとして機能できるようにする
- dnsmasq : DNSサーバのフォワーダとDHCPサーバをもつソフトウェア

### サービスを停止

```sh
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```

### DHCPサーバー（dnsmasq）の設定

設定ファイルのバックアップ

```sh
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
```

新しい設定ファイルを作成 ( /etc/dnsmasq.conf  ) 

wlan0のインタフェースに対して、192.168.4.2 ~ 192.168.4.20 までのアドレスを配布するように設定

```conf
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
```

### ネットワークインターフェースの静的IPアドレス設定

設定ファイルに以下の内容を追加 ( /etc/dhcpcd.conf )

wlan0のインタフェースに対して、固定IP 192.168.4.1 を設定

 ```conf
interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant
 ```

### アクセスポイント（hostapd）の設定

設定ファイルに以下の内容を追加 ( /etc/hostapd/hostapd.conf )

wlan0をアクセスポイントとして定義し、SSID・パスワードを以下に設定

- SSID : intern2024
- PASSWORD : password2024

```conf
interface=wlan0
driver=nl80211
ssid=intern2024
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=password2024
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```

### hostapd設定ファイルの場所を指定

設定ファイルに以下の内容を追加 ( /etc/default/hostapd )

```conf
DAEMON_CONF="/etc/hostapd/hostapd.conf"
```

### IPフォワーディングの有効化

設定ファイルに以下の内容を追加 ( /etc/sysctl.conf )

```conf
net.ipv4.ip_forward=1
```

### NATテーブルルールの設定

```sh
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```

### iptablesルールを起動時に適用

起動ファイルに以下を追加 ( /etc/rc.local )

```conf
iptables-restore < /etc/iptables.ipv4.nat
```

### サービスを再起動

```sh
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd
sudo systemctl start dnsmasq
```

## Webサーバの起動方法

### インストール

任意のディレクトリに、[server.py](server.py)をコピーし、パッケージをインストール

```sh
pip3 install flask==3.0.3
```

### 実行

python3で実行

```sh
python3 server.py
```

## 元に戻す方法

### "hostapd"と"dnsmasq"のサービスを停止する

```sh
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq
```

### "hostapd"と"dnsmasq"のアンインストール

```sh
sudo apt-get purge hostapd dnsmasq -y
```

### 設定ファイルの削除

```sh
sudo rm /etc/hostapd/hostapd.conf
sudo rm /etc/dnsmasq.conf
```

### DHCPサーバー（dnsmasq）の設定復元

設定ファイル ( /etc/dhcpcd.conf ) の以下の行を削除

```conf
interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant
```

### ネットワークインタフェースの再起動

```sh
sudo systemctl restart dhcpcd
```

### iptablesルールの削除

NATテーブルルールを削除します。

```sh
sudo iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"
```

### rc.localの復元

rc.localファイルからiptables-restoreの行を削除します。

```sh
iptables-restore < /etc/iptables.ipv4.nat
```

### hostapdとdnsmasqのサービスを無効にする

```sh
sudo systemctl disable hostapd
sudo systemctl disable dnsmasq
```

### 再起動

最後に、システムを再起動して変更を適用します。

```sh
sudo reboot
```

これで、Raspberry Piは元の状態に戻ります。