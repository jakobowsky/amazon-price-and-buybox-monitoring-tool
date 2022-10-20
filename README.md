Get information about prices, sellers and buybox winnders for different ASINs using Selling Partner API
[Watch full video here](https://youtu.be/wX0lqhQZR1g)

#
![buybox_thumbnail](https://user-images.githubusercontent.com/32365708/196908346-90a40f03-f431-4f41-b036-d59c44ed6aeb.jpg)
<img width="956" alt="Screenshot 2022-10-20 at 11 18 32" src="https://user-images.githubusercontent.com/32365708/196909259-9939fbfe-f364-4651-8258-c15c3a7169f6.png">
<img width="2485" alt="Screenshot 2022-10-20 at 11 18 49" src="https://user-images.githubusercontent.com/32365708/196909346-49aaded5-3b11-4388-b1f2-b5e7cffb7a51.png">
#


## Setup Python Virtual Environment
```buildoutcfg
pipenv install
pipenv shell
```
## Running Script

```buildoutcfg
#create and fill credentials in .env
python manage.py migrate
python manage.py runserver
```

## Monitoring tool script

```buildoutcfg
python manage.py get_data_from_amazon
```
