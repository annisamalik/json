from flask import Flask

app = Flask(__name__)

produk = {
  "laptop": [
    {
      "id": 1,
      "nama_produk": "Macbook Air",
      "harga_produk": 15000000,
      "url_img": "https://cdn.mos.cms.futurecdn.net/TaicKGcS88HAJ9eHtx6JwH-970-80.jpg",
      "stok" : 10
    },
    {
      "id": 2,
      "nama_produk": "Macbook Pro",
      "harga_produk": 30000000,
      "email": "https://sm.pcmag.com/t/pcmag_ap/review/a/apple-macb/apple-macbook-pro-16-inch_e1zs.640.jpg",
      "stok" : 20
    },
    {
      "id": 3,
      "nama_produk": "iMac",
      "harga_produk": 20000000,
      "email": "https://ibox.co.id/media/catalog/product/cache/3/image/9df78eab33525d08d6e5fb8d27136e95/i/m/imac-27-cto-hero-201903_1_1.jpeg",
      "stok" : 50
    }
  ]
}

data_keranjang = {
    "iPhone XR": {"jumlah": 3, "harga": 15000000},
    "iPad 7": {"jumlah": 5, "harga": 5000000},
    "Macbook Air": {"jumlah" : 1, "harga": 13000000}
}

@app.route('/keranjang')
def tampil_keranjang():
    if len(data_keranjang)==0:
        return {
            "chats": [
                {
                    "text" : "Keranjang belanja anda masih kosong",
                    "type" : "text"
                }
            ]
        }
    else:
        listkeranjang = ""
        totalharga = 0
        for produk in data_keranjang:
            listkeranjang = listkeranjang+str(produk)+" - "+str(data_keranjang[produk]["harga"])+" Jumlah:"+str(data_keranjang[produk]["jumlah"])+"\n"
            totalharga = totalharga+ (data_keranjang[produk]["harga"]*data_keranjang[produk]["jumlah"])
        return {
            "chats": [
                {
                    "text" : str(listkeranjang) + "Total belanja kamu adalah "+str(totalharga),
                    "type" : "text"
                }
            ]
        }



if __name__ == "__main__":
    app.run()
