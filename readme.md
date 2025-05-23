# Порівняння алгоритмів сортування: злиттям, вставками та Timsort за часом виконання

## Відповідні алгоритми описані у функціях:

merge_sort - алгоритм сортування злиттям  
insertion_sort - сортування вставками  
sorted - Timsort

# Тести алгоритмів

Тест витраченого часу на виконання сортування використовуючи різні аргументи проводився на 4 типах масивів:

1.  sorted_array - відсортований масив, що складається з 10000 чисел
2.  lightly_unsorted_array - масив, що потребує 1 операцію сортування в ідеальному випадку. Тобто відсортований масив з 9998 чисел, що має 2 не відсортованих числа на початку ([**2**,**1**, 3,4,5,6,7 ... ]).
3.  control_array - не відсортований масив, що складається з 10000 чисел, але однаковий для всіх алгоритмів. Контрольний випадок для порівняння, як алгоритми справляються з однаковими вхідними даними.
4.  random_array - не відсортований масив, що складається з 10000 чисел, але різний для всіх алгоритмів.

У випадку тестування random_array генерувалось 10 таких масивів індивідуально для кожного алгоритму та вираховувався середній час сортування для всіх масивів.

Час виконання замірявся бібліотекою timeit.

## Tecт 1

**insertion_sort**  
`sorted_array` : 0.0006045409245416522  
`lightly_unsorted_array` : 0.0006006669718772173  
`control_array` : 1.0550895830383524  
`random_array` : 1.0479241583030672  
**merge_sort**  
`sorted_array` : 0.011069125030189753  
`lightly_unsorted_array` : 0.010980374994687736  
`control_array` : 0.013698708033189178  
`random_array` : 0.013822300022002309  
**sorted**  
`sorted_array` : 4.0874932892620564e-05  
`lightly_unsorted_array` : 4.7291978262364864e-05  
`control_array` : 0.0007875829469412565  
`random_array` : 0.0007891749963164329

## Tecт 2

**insertion_sort**  
`sorted_array` : 0.0005156249972060323  
`lightly_unsorted_array` : 0.0005083750002086163  
`control_array` : 0.9866519590141252  
`random_array` : 1.053615112695843  
**merge_sort**  
`sorted_array` : 0.011039625038392842  
`lightly_unsorted_array` : 0.010965083027258515  
`control_array` : 0.01369979209266603  
`random_array` : 0.013862066611181945  
**sorted**  
`sorted_array` : 3.9874925278127193e-05  
`lightly_unsorted_array` : 4.529103171080351e-05  
`control_array` : 0.0007909999694675207  
`random_array` : 0.0007896207855083049

## Tecт 3

**insertion_sort**  
`sorted_array` : 0.0005169999785721302  
`lightly_unsorted_array` : 0.0005079170223325491  
`control_array` : 0.9871784580172971  
`random_array` : 1.0503205542103387  
**merge_sort**  
`sorted_array` : 0.01103795797098428  
`lightly_unsorted_array` : 0.010945792077109218  
`control_array` : 0.013675000052899122  
`random_array` : 0.01383048330899328  
**sorted**  
`sorted_array` : 4.004104994237423e-05  
`lightly_unsorted_array` : 3.933301195502281e-05  
`control_array` : 0.0008027500007301569  
`random_array` : 0.0007876460906118155

## Tecт 4

**insertion_sort**  
`sorted_array` : 0.0005155419930815697  
`lightly_unsorted_array` : 0.0005061670672148466  
`control_array` : 0.9903228749753907  
`random_array` : 1.0546947331284173  
**merge_sort**  
`sorted_array` : 0.011060917051509023  
`lightly_unsorted_array` : 0.01096337498165667  
`control_array` : 0.013820791966281831  
`random_array` : 0.013932075002230704  
**sorted**  
`sorted_array` : 4.170800093561411e-05  
`lightly_unsorted_array` : 3.99579294025898e-05  
`control_array` : 0.000821709050796926  
`random_array` : 0.0008119170204736292

## Tecт 5

**insertion_sort**  
`sorted_array` : 0.0005299589829519391  
`lightly_unsorted_array` : 0.0005244590574875474  
`control_array` : 0.9961349160876125  
`random_array` : 1.0479638376040383  
**merge_sort**  
`sorted_array` : 0.011048584012314677  
`lightly_unsorted_array` : 0.010957875056192279  
`control_array` : 0.01372454094234854  
`random_array` : 0.013845570792909712  
**sorted**  
`sorted_array` : 4.0082959458231926e-05  
`lightly_unsorted_array` : 4.7332956455647945e-05  
`control_array` : 0.0007847920060157776  
`random_array` : 0.0007882500067353249

## Середні значення тестів

**insertion_sort**  
`sorted_array` : 0.0005365333752706646  
`lightly_unsorted_array` : 0.0005295170238241553  
`control_array` : 1.0030755582265556  
`random_array` : 1.0509036791883408  
**merge_sort**  
`sorted_array` : 0.011051241820678116  
`lightly_unsorted_array` : 0.010962500027380884  
`control_array` : 0.01372376661747694  
`random_array` : 0.01385849914746359  
**sorted**  
`sorted_array` : 4.0516373701393604e-05  
`lightly_unsorted_array` : 4.384138155728578e-05  
`control_array` : 0.0007975667947903275  
`random_array` : 0.0007933217799291015

# Висновок

Порівнюючи результати тесту, якщо відсортувати алгоритми за часом виконання по запропонованим типам списків, то ми отримаємо наступну таблицю:

| Array type                 |             Algorythms             |
| -------------------------- | :--------------------------------: |
| **sorted_array**           | sorted, insertion_sort, merge_sort |
| **lightly_unsorted_array** | sorted, insertion_sort, merge_sort |
| **control_array**          | sorted, merge_sort, insertion_sort |
| **random_array**           | sorted, merge_sort, insertion_sort |

Згідно з таблицею вище, можна зробити висновок, що алгоритм Timsort працює найшвидше для всіх типів масивів: відсортованих, з рандомними даними та масивів, що потребують 1 операцію сортування в ідеальному випадку.
Для алгоритмів сортування злиттям та вставками можна виділити наступний висновок. Алгоритм вставками краще працює, якщо ми маємо вже відсортований масив або масив, що потребує 1 операцію сортування в ідеальному випадку. Алгоритм сортування злиттям в такому випадку працює гірше, але швидше справляється з масивами, що складаються з випадкового набору чисел.

Отже згідно з цим дослідженням емпірично було доведено що:

- Алгоритм сортування вставками дуже повільний на випадкових даних , що відповідає його теоретичній складності O(n\*\*2).Однак він відносно швидкий на вже відсортованих або майже відсортованих даних, що відповідає його складності O(n) у кращому випадку.
- Сортування злиттям - демонструє стабільну продуктивність O(n\*log(n)) на всіх типах масивів, значно випереджаючи алгоритм сортування вставками на випадкових даних, але поступаючись йому на відсортованих/майже відсортованих.
- Вбудована функція sorted (Timsort) показує найкращі результати на всіх типах масивів. Вона значно швидша за merge_sort та insertion_sort у всіх сценаріях. Це емпірично доводить ефективність поєднання підходів у Timsort.
