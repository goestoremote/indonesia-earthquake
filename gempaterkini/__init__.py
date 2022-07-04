import requests
from bs4 import BeautifulSoup


def ekstrasi_data():
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('span',{'class':'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div',{'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        magnitude = None
        kedalaman = None
        koordinat = None
        lokasi = None
        dirasakan = None
        i = 0
        for res in result:
            # print (i,res)
            if i == 1 :
                magnitude = res.text
            elif i == 2 :
                kedalaman = res.text
            elif i == 3 :
                koordinat = res.text.split(' - ')
                lu = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5 :
                dirasakan = res.text
            i = i + 1


        hasil = dict()
        hasil['Tanggal'] = tanggal
        hasil['Waktu'] = waktu
        hasil['magnitude'] = magnitude
        hasil['koordinat'] = {'lu': lu, 'bt' : bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilan_data(result):
    if result is None:
        print("Tidak bisa menampilkan data")
        return

    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal     {result['Tanggal']}")
    print(f"Waktu       {result['Waktu']}")
    print(f"Koordinat   {result['koordinat']['lu']} {result['koordinat']['bt']}")
    print(f"Magnitude   {result['magnitude']}")
    print(f"Lokasi      {result['lokasi']}")
    print(f"Dirasakan   {result['dirasakan']}")

if __name__ == '__main__':
    result = ekstrasi_data()
    tampilan_data(result)