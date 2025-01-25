## Условие 
### :Вам нужно написать функцию расчёта стоимости доставки.

Стоимость рассчитывается в зависимости от:

*расстояния до пункта назначения:*

- более 30 км: +300 рублей к доставке;
- до 30 км: +200 рублей к доставке;
- до 10 км: +100 рублей к доставке;
- до 2 км: +50 рублей к доставке;

 

*габаритов груза:*

- большие габариты: +200 рублей к доставке;
- маленькие габариты: +100 рублей к доставке;

 

*хрупкости груза.* Если груз хрупкий — +300 рублей к доставке. Хрупкие грузы нельзя возить на расстояние более 30 км;

 

*загруженности службы доставки*. Стоимость умножается на коэффициент доставки:

- очень высокая загруженность — 1.6;
- высокая загруженность — 1.4;
- повышенная загруженность — 1.2;
- во всех остальных случаях коэффициент равен 1.

 

Минимальная сумма доставки — 400 рублей. Если сумма доставки меньше минимальной, выводится минимальная сумма.

На входе функция получает расстояние до пункта назначения, габариты, информацию о хрупкости, загруженность службы на текущий момент. На выходе пользователь получает стоимость доставки.

 

### Что нужно сделать:

1. напишите код-решение для этой задачи;
2. покройте своё решение автотестами. Ответ приложите в виде ссылки на репозиторий;
3. ответьте на вопросы: 
   - Как бы вы тестировали/проверяли корректность, полноту и неизбыточность ваших тестов?
   - Как бы вы осуществляли эти проверки в автоматическом режиме?
   - Почему вы хотите стать ревьюером в Яндекс Практикуме?
   - Как вы учились тестированию и попали в эту профессию?*.*
## Как запустить тесты

```bash
python -m venv /path/to/new/virtual/environment
pip install -r requirements.txt
pytest test/test_delivery_cost.py -v
```

## Пример успешного выполнения тестов
```bash
(venv) C:\Users\leonn\PycharmProjects\yandex_prakticum_test_task>pytest test/test_delivery_cost.py -v
================================================================================ test session starts ================================================================================
platform win32 -- Python 3.8.6, pytest-8.3.4, pluggy-1.5.0 -- c:\users\leonn\pycharmprojects\yandex_prakticum_test_task\venv\scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\leonn\PycharmProjects\yandex_prakticum_test_task
collected 9 items                                                                                                                                                                    

test/test_delivery_cost.py::TestDeliveryCost::test_delivery_distance[delivery_distance=-1] PASSED                                                                              [ 11%]
test/test_delivery_cost.py::TestDeliveryCost::test_delivery_distance[delivery_distance=1] PASSED                                                                               [ 22%]
test/test_delivery_cost.py::TestDeliveryCost::test_delivery_distance[delivery_distance=2] PASSED                                                                               [ 33%]
test/test_delivery_cost.py::TestDeliveryCost::test_delivery_distance[delivery_distance=15] PASSED                                                                              [ 44%]
test/test_delivery_cost.py::TestDeliveryCost::test_delivery_distance[delivery_distance=35] PASSED                                                                              [ 55%]
test/test_delivery_cost.py::TestDeliveryCost::test_minimal_cost_threshold PASSED                                                                                               [ 66%]
test/test_delivery_cost.py::TestDeliveryCost::test_fragile_cargo_delivery_distance_limit[delivery_distance=10] PASSED                                                          [ 77%]
test/test_delivery_cost.py::TestDeliveryCost::test_fragile_cargo_delivery_distance_limit[delivery_distance=350] PASSED                                                         [ 88%]
test/test_delivery_cost.py::TestDeliveryCost::test_high_cost_delivery PASSED                                                                                                   [100%]

================================================================================= 9 passed in 0.03s =================================================================================

(venv) C:\Users\leonn\PycharmProjects\yandex_prakticum_test_task>

```