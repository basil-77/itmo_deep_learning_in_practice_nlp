# Мэтчинг: резюме - вакансия

Данный проект выполнен в рамках курса "Глубокое обучение на практике" от магистратуры ITMO AI Talent Hub.

## Основная идея

Загружаем резюме через веб-сервис, получаем описание, информацию об основных навыках и опыте работы. Этот текст отправляем в заранее обученную модель. На выходе модели получаем summary, то есть наименование профессии. Это summary передаем через API на сайты поиска работы (hh.ru или trudvsem.ru) и ищем вакансии по нашему запросу.

## Описание используемых данных

За основу был взят [датасет вакансий](https://disk.yandex.ru/d/1bt0KXaLjlo8VA) с "hh.ru". Очищенный от лишних столбцов, датасет представляет из себя таблицу:

<p align="center"><img src="image/1.jpg" width=95% alt="Main page"></p>

То есть столбец с названием вакансии и столбец с ее описанием.

## Inference 

Обученная на описанном выше датасете модель загружена в репозиторий Hugging Face и доступна по [ссылке](https://huggingface.co/basil-77/rut5-base-absum-vacancieshh). Либо по QR-коду:

<p align="center"><img src="image/2.jpg" width=30% alt="Main page"></p>

 Обращение к модели производится путем вызова стандартных методов пакета transformers и предварительного скачивания модели/весов не требует:

 ```
import torch  
from transformers import T5ForConditionalGeneration, T5Tokenizer
```

```
MODEL_NAME = 'basil-77/rut5-base-absum-hh'
model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
model.eval();
 ```


## MVP

Продукт представляет собой веб-сервис.

Веб-приложение позволяет загрузить своё резюме в формате PDF и получить на выходе подборку вакансий с hh.ru с численным значением "score" - на сколько подходит вакансия под загруженное резюме.

Запись работы приложения:

[![Watch the video](https://i.stack.imgur.com/Vp2cE.png)](https://www.youtube.com/watch?v=u-sN-B2MxCc)

- Веб-приложение: streamlit
- Модель: rut5-base absum

## Как запустить веб-сервис

### Requirements >= 3.10 python version <=3.11
```bash
pip install -r requirements.txt
```

### Запуск из папки проекта
```bash
streamlit run app.py
```
