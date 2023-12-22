# Мэтчинг: резюме - вакансия

Данный проект выполнен в рамках курса "Глубокое обучение на практике" от магистратуры ITMO AI Talent Hub.

## Основная идея

Загружаем резюме через веб-сервис, получаем описание, информацию об основных навыках и опыте работы. Этот текст отправляем в заранее обученную модель. На выходе модели получаем summary, то есть наименование профессии. Это summary передаем через API на сайты поиска работы (hh.ru или trudvsem.ru) и ищем вакансии по нашему запросу.

## Описание используемых данных

За основу был взят [датасет вакансий](https://drive.google.com/file/d/1ikA_Ht45fXD2w5dWZ9sGTSRl-UNeCVub/view) с "hh.ru". Датасет представляет из себя таблицу:

<p align="center"><img src="image/1.jpg" width=95% alt="Main page"></p>

Подробное EDA данного датасета с одноименным названием находится в отдельной ветке репозитория.

## Inference 

[Модель](https://huggingface.co/basil-77/rut5-base-absum-vacancieshh) находится на Hugging Face, вся обработка происходит там. QR код:

<p align="center"><img src="image/2.jpg" width=30% alt="Main page"></p>

## MVP

Продукт представляет собой веб-сервис.

Веб-приложение позволяет загрузить своё резюме в формате PDF и получить на выходе подборку вакансий с hh.ru с численным значением "score" - наиболее подходящая вакансия под загруженное резюме.

Запись работы приложения:

[<p align="center"><img src="https://img.youtube.com/vi/u-sN-B2MxCc/hqdefault.jpg" width=90%
/>](https://www.youtube.com/watch?v=u-sN-B2MxCc)

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
