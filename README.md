Описание
=======

Поиск слов в словаре, из букв которых можно составить другие слова из этого же словаря.

MIN_WORD_LENGTH - минимальное кол-во букв, которое должно быть в полученных словах.

MIN_PERMUTATIONS - минимальное кол-во полученных слов.

PREFIX_LENGTH - длина префикса для ускорения поиска полученных слов в префиксном дереве.


Алгоритм
=======

Сохраняем слова в префиксное дерево для быстрого поиска существующих слов.

Далее в цикле проходим по словарю.

Для каждого слова собираем массив из валидных префиксов с помощью дерева.

Например, слово "авторство". Через itertools.permutations получаем перестановки
длиной PREFIX_LENGTH и проверяем существование префикса в дереве.

"авто" - такой префикс найден, сохраняем его,
"втоа" - а такого префикса нет, значит по нему и искать более длинные слова смысла нет.

Далее уже ищем слова длиной MIN_WORD_LENGTH, для которых уже есть сохраненные префиксы.
