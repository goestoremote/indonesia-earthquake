# indonesia-earthquake
this project will report the latest earthquake in Indonesia from BADAN METEOROLOGI, KLIMATOLOGI, DAN GEOFISIKA

## HOW IT WORK?

This package will scrape data from [BMKG](https://bmkg.go.id/) to get the latest earthquake happen in Indonesia

This package use BeautifulSoup4 and requests package to scrape data.

## HOw TO USE

Install package use: pip install earthquake-id-warning
```
import gempaterkini

if __name__ == '__main__':
    result = gempaterkini.ekstrasi_data()
    gempaterkini.tampilan_data(result)
```

## Author
Heru Setiawan
