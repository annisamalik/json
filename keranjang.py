from flask import Flask, request, jsonify

app = Flask(__name__)



pesanan = {}

produk = {
  "laptop":
      { "list_barang" : [
    {
      "id": 1,
      "nama_produk": "Macbook Air",
      "harga_produk": 15000000,
      "promo" : True,
      "url_img": "https://cdn.mos.cms.futurecdn.net/TaicKGcS88HAJ9eHtx6JwH-970-80.jpg",
      "stok" : 10
    },
    {
      "id": 2,
      "nama_produk": "Macbook Pro",
      "harga_produk": 30000000,
      "promo": False,
      "url_img": "https://sm.pcmag.com/t/pcmag_ap/review/a/apple-macb/apple-macbook-pro-16-inch_e1zs.640.jpg",
      "stok" : 20
    },
    {
      "id": 3,
      "nama_produk": "iMac",
      "harga_produk": 20000000,
      "promo": False,
      "url_img": "https://ibox.co.id/media/catalog/product/cache/3/image/9df78eab33525d08d6e5fb8d27136e95/i/m/imac-27-cto-hero-201903_1_1.jpeg",
      "stok" : 50
    }
  ],
      "url_img" : "",
      "keterangan" : ""},
  "iPad":
      { "list_barang" : [
    {
      "id": 1,
      "nama_produk": "iPad Air 2019",
      "harga_produk": 8000000,
      "promo": False,
      "url_img": "https://www.gizmochina.com/wp-content/uploads/2019/03/Apple-iPad-Air-2019-500x500.jpg",
      "stok" : 10
    },
    {
      "id": 2,
      "nama_produk": "iPad 7",
      "harga_produk": 5000000,
      "promo" : True,
      "url_img": "https://s.blanja.com/picspace/56/305208/700.462_e3cc17e2d3ae4faa8102dcb0435bba35.jpg",
      "stok" : 20
    },
    {
      "id": 3,
      "nama_produk": "iPad Pro",
      "harga_produk": 20000000,
      "promo": False,
      "url_img": "https://icdn3.digitaltrends.com/image/digitaltrends/ipad-pro-2018-review-5848-768x479-c.jpg",
      "stok" : 50
    }
  ],
      "url_img" : "",
      "keterangan" : ""},
"iPhone":
      { "list_barang" : [
    {
      "id": 1,
      "nama_produk": "iPhone XR",
      "harga_produk": 10000000,
      "promo" : True,
      "url_img": "https://p.ipricegroup.com/uploaded_a545ecc174943263565ec786c03b9fdf.jpg",
      "stok" : 10
    },
    {
      "id": 2,
      "nama_produk": "iPhone 11",
      "harga_produk": 10000000,
      "promo": False,
      "url_img": "https://id-test-11.slatic.net/p/abbbe4a6e24b6658229755b18352e254.jpg",
      "stok" : 20
    },
    {
      "id": 3,
      "nama_produk": "iPhone 11 Pro",
      "harga_produk": 15000000,
      "promo": False,
      "url_img": "https://p.ipricegroup.com/uploaded_df23273ab706197931c6092e3b2b40e5.jpg",
      "stok" : 50
    }
  ],
      "url_img" : "",
      "keterangan" : ""}
}

data_keranjang = {
    "iPhone XR": {"jumlah": 3, "harga": 15000000, "url": "https://p.ipricegroup.com/uploaded_a545ecc174943263565ec786c03b9fdf.jpg"},
    "iPad 7": {"jumlah": 5, "harga": 5000000, "url" : "https://s.blanja.com/picspace/56/305208/700.462_e3cc17e2d3ae4faa8102dcb0435bba35.jpg"},
    "Macbook Air": {"jumlah" : 1, "harga": 13000000, "url" : "https://cdn.mos.cms.futurecdn.net/TaicKGcS88HAJ9eHtx6JwH-970-80.jpg"}
}
"""
@app.route('/kategori')
def tampil_kategori():
    coba = []
    for kategori in produk:
        print(kategori)


    return kategori
"""
@app.route('/<kategori>')
def tampil_produk(kategori):
    kolom = []
    for i in range(len(produk[kategori]["list_barang"])):
        lagi_promo = ""
        if produk[kategori]["list_barang"][i]["promo"]:
            lagi_promo = "BARANG SEDANG PROMO"
        if produk[kategori]["list_barang"][i]["stok"] > 0:
            info_produk = {
                "title": produk[kategori]["list_barang"][i]["nama_produk"],
                "text": "Rp{:,.2f}".format(produk[kategori]["list_barang"][i]["harga_produk"]) + "\nStok :" + str(produk[kategori]["list_barang"][i]["stok"]) + "\n" + lagi_promo,
                "image_url": produk[kategori]["list_barang"][i]["url_img"],
                "buttons": [
                {
                    "label": "Beli",
                    "type": "path",
                    "path": "5ed9ebd020f8374bf65abbe6",
                    "variable": {
                        "nama_produk": produk[kategori]["list_barang"][i]["nama_produk"],
                        "harga_produk": "Rp{:,.2f}".format(produk[kategori]["list_barang"][i]["harga_produk"])
                    }
                },
                {
                    "label": "Kembali",
                    "type": "path",
                    "path": "5ed5f3ac20f8374bf65aa6a5"
                }
                ],
                "type": "button"
            }
            kolom.append(info_produk)


    return {
        "chats": [
            {
                "columns": kolom,
                "type": "carousel"
            }
        ]
        }

@app.route('/promo')
def tampil_promo():
    kolom = []
    for kategori in produk:
        for barang in produk[kategori]["list_barang"]:
            lagi_promo = ""
            if barang["promo"]:
                lagi_promo = "BARANG SEDANG PROMO"
            if barang["stok"] > 0 and barang["promo"]:
                info_produk = {
                    "title": barang["nama_produk"],
                    "text": "Rp{:,.2f}".format(barang["harga_produk"]) + "\nStok :" + str(
                        barang["stok"]) + "\n" + lagi_promo,
                    "image_url": barang["url_img"],
                    "buttons": [
                        {
                            "label": "Beli",
                            "type": "path",
                            "path": "5ed9ebd020f8374bf65abbe6",
                            "variable": {
                                "nama_produk": barang["nama_produk"],
                                "harga_produk": "Rp{:,.2f}".format(barang["harga_produk"])
                            }
                        },
                        {
                            "label": "Kembali",
                            "type": "path",
                            "path": "5ed5f3ac20f8374bf65aa6a5"
                        }
                    ],
                    "type": "button"
                }
                kolom.append(info_produk)

    return {
        "chats": [
            {
                "columns": kolom,
                "type": "carousel"
            }
        ]
    }

@app.route('/tampil_kategori')
def tampil_kategori():
    kolom = []
    for kategori in produk:
        stok = 0
        print(kategori)
        for barang in produk[kategori]["list_barang"]:
            stok += barang["stok"]
        if stok > 0:
            info_produk = {
                "title": kategori,
                "text": produk[kategori]["keterangan"],
                "image_url": produk[kategori]["url_img"],
                "buttons": [
                    {
                        "label": "Cari",
                        "type": "path",
                        "path": "5ed9ebd020f8374bf65abbe6",
                        "variable": {
                            "kategori": kategori
                        }
                    },
                    {
                        "label": "Kembali",
                        "type": "path",
                        "path": "5ed5f3ac20f8374bf65aa6a5" #ke menu greeting atau menu
                    }
                ],
                "type": "button"
            }
            kolom.append(info_produk)

    return {
        "chats": [
            {
                "columns": kolom,
                "type": "carousel"
            }
        ]
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
                    "text" : str(listkeranjang) + "\nTotal belanja kamu adalah "+str(totalharga),
                    "type" : "text"
                }
            ]
        }

@app.route('/carousel_keranjang')
def carousel_keranjang():
    kolom = []
    for produk in data_keranjang:
        info_produk = {
            "title": str(produk),
            "text": "Rp{:,.2f}".format(data_keranjang[produk]["harga"]) + "\nJumlah :" + str(data_keranjang[produk]["jumlah"]),
            "image_url": data_keranjang[produk]["url"],
            "buttons": [
                {
                    "label": "Hapus Semua",
                    "type": "path",
                    "path": "5ee09a4e20f837185ebed3a3",
                    "variable": {
                        "nama_produk": produk
                    }
                },
                {
                    "label": "Ubah Jumlah",
                    "type": "path",
                    "path": "5ee09c9420f837185ebed3d5",
                    "variable": {
                        "nama_produk": produk
                    }
                },
                {
                    "label": "Kembali",
                    "type": "path",
                    "path": "5ed6082520f8374bf65aa742"
                }
            ],
            "type": "button"
        }
        kolom.append(info_produk)

    return {
        "chats": [
            {
                "columns": kolom,
                "type": "carousel"
            }
        ]
    }

@app.route('/keranjang/hapus/', methods=['POST'])
##contoh bentuk body request {"nama_produk" : "Macbook Air"}
def hapus_keranjang():
    hapus_produk = request.json['nama_produk']
    # I.S : Produk sudah ada di keranjang
    if data_keranjang[hapus_produk]["jumlah"] > 1 :
        data_keranjang[hapus_produk]["jumlah"] -= 1
    else:
        del data_keranjang[hapus_produk]
    return jsonify({"data_keranjang" : data_keranjang})


@app.route('/keranjang/tambah/', methods=['POST'])
##contoh bentuk body request {"nama_produk" : "Macbook Air", "harga_produk" : 13000000}
def tambah_keranjang():
    input_produk = { "nama_produk" : request.json['nama_produk'], "harga_produk" : request.json['harga_produk']}
    if input_produk["nama_produk"] in data_keranjang :
        data_keranjang[input_produk["nama_produk"]]["jumlah"] += 1
    else:
        data_keranjang[input_produk["nama_produk"]] = {"jumlah": 1, "harga": input_produk["harga_produk"]}
        print(data_keranjang)
    return jsonify({"data_keranjang" : data_keranjang})




if __name__ == "__main__":
    app.run()
