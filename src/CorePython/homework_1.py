#!/usr/bin/python3

# ! TASK 1
# Տրված է թվաբանական պրոգրեսիայի առաջին եւ երկրորդ անդամները։ Տրված n֊ի համար, 
# վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։

def progression(a, b, n):
    k = b - a
    for i in range(1, n):
        a = a + k  # amen angam a mecanum a 'k' gorcakcov
    return a


def dprogression(a, b, n):
    return a + (n - 1) * (b - a)


x = dprogression(1, 4, 12)
print(x)


# ! TASK 2
# CodeMaster-ը նոր է վերադարձել գնումներից։ Նա սկանավորեց իր գնած ապրանքների չեկը եւ 
# ստացված շարանը տվեց Ratiorg֊ին՝ պարզելու գնված ապրանքների ընդհանուր թիվը: Քանի 
# որ Ratiorg-ը բոտ է, նա անպայման պատրաստվում է այն ավտոմատացնել, ուստի նրան անհրաժեշտ է 
# ծրագիր, որը կամփոփի բոլոր թվերը, որոնք հայտնվում են տվյալ մուտքագրում:
# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում հայտնված թվերի գումարը։


def str_sum(string):
    ans = 0
    ls = string.split()
    for a in ls:
        if a.isnumeric():
            ans += int(a)
    return ans


# ! TASK 3
# Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են ոչ աճող կամ 
# չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ դեփքում:

def is_sorted(a, b, c):
    if a >= b >= c or a <= b <= c:
        print("Sorted")
    else:
        print("Unsorted")


# ! TASK 4
# Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն կատարյալ թիվ է, թե ոչ։
# Հ Գ Թիվը կոչվում է կատարյալ, եթե այն հավասար է իր բաժանարարների գումարին։

def is_perfect(n):
    sm = 0
    for i in range(1, n // 2 + 1):
        if not n % i:
            sm += i
    return sm == n


# ! TASK 5
# Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա էլեմենտների գումարը։

def list_sum(ls: list):
    ans = 0
    for a in ls:
        ans += a
    return ans


# ! TASK 6
# Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ ցուցակի ամենամեծ էլեմենտը։

def list_max(ls: list):
    if len(ls) == 0:
        return
    ans = ls[0]
    for a in ls:
        if a > ans:
            ans = a
    return ans


# ! TASK 7
# Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր էլեմենտները։

def list_remove(ls: list, n):
    for i in range(len(ls) - 1, 0, -1):
        if ls[i] == n:
            ls.remove(ls[i])
    return ls


def list_rm(ls: list, n):
    counter = 0
    for i in ls:
        if i == n:
            counter += 1
    for i in range(counter):
        ls.remove(n)
    return ls


def list_rem(ls: list, n):
    ret = []
    for i in ls:
        if i != n:
            ret.append(i)
    return ret


print(list_rem([1, 2, 3, 1, 1], 1))


# ! TASK 8
# Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր էլեմենտների արտադրյալը։

def list_mult(ls: list):
    ans = 1
    for a in ls:
        ans *= a
    return ans


# ! TASK 9
# Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի բազմապատիկ է։

def rev_str(string):
    if not len(string) % 4:
        return string[::-1]


# ! TASK 10
# Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ անդամը։
# Խնդիրը լուծել եւ ռեկուրսիվ, եւ իտերատիվ մեթոդներով։

def fibonacci_iter(n: int) -> int:
    """իտերատիվ եղանակ"""
    prev = 0
    curr = 1
    for _ in range(1, n):
        curr += prev
        prev = curr - prev
    return curr


def fibonacci_rec(n: int) -> int:
    """ռեկուրսիվ եղանակ"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


# ! TASK 11
# Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց ամենափոքր 
# ընդհանուր բազմապատիկը։

def is_prime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def divisors(n):
    a = n
    ls = []
    while not is_prime(a):
        for i in range(2, a):
            if not a % i:
                ls.append(i)
                a //= i
                break
    ls.append(a)
    return ls


def operator_or(ls1: list[int], ls2: list[int]) -> list[int]:
    """ls1 U ls2"""
    for item in ls1:
        if item in ls2:
            ls2.remove(item)
    return ls1 + ls2


def common_mult(a: int, b: int):
    """լուծման ճիշտ եղանակ"""
    ls = operator_or(divisors(a), divisors(b))
    ans = 1
    for item in ls:
        ans *= item
    return ans


def common_mult2(a, b):
    """լուծման հեշտ եղանակ"""
    small, big = (a, b) if a < b else (b, a)
    i = 1
    while i * small % big:
        i += 1
    return i * small


# ! TASK 12
# Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:
#  Օրինակ 119-ի համար հաջորդ պալինդրոմը 121 է

def is_palindrome(n):
    st = str(n)
    return st == st[::-1]


def next_palindrome(n):
    n += 1  # եթե n-ը ինքնին պալինդրոմ լինի, ապա մեզ պետք է «հաջորդ» պալինդրոմը, ոչ թե հենց ինքը
    while not is_palindrome(n):
        n += 1
    return n


# ! TASK 13
# Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա եւ ներկայումս գտնվում է կետում (X0, Y0): 
# Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման հրամաններ:
# Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման ստանալուց հետո 
# ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե ռոբոտը սխալ հրաման է 
# ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:
# Ուշադրություն: աջը՝ x0+1, ձախը՝ x0-1, վերեւը՝ y0+1, ներքեւը՝ y0-1։

def robot_moves(start: tuple[int, int], *argv) -> tuple:
    X0, Y0 = start
    for command in argv:
        match command:
            case "up":
                Y0 += 1
            case "down":
                Y0 -= 1
            case "right":
                X0 += 1
            case "left":
                X0 -= 1
            case _:
                continue
    return X0, Y0


# ! TASK 14
# Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են: Օրինակ
# Ցուցակ1 = [1,2,3,4,5,6]
# Ցուցակ2 = [6,1,2,3,4,5]
# Վերադարձել True

def one_step_cycle(l1, l2):
    if len(l1) != len(l2):
        return False
    left, right = (l1, l2) if l1[0] == l2[1] else (l2, l1)
    for i in range(len(right)):
        if right[i] != left[i - 1]:
            return False
    return True


# ! TASK 15
# Գրել ծրագիր, որը ստանում է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
# ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:

def delete_digit(n):
    ans = 0
    ls = list(str(n))
    rm_flag = True
    for i in range(len(ls) - 1):
        if ls[i] < ls[i + 1]:
            ls.remove(ls[i])
            rm_flag = False
            break
    if rm_flag:  # եթե ոչ մի նիշ չենք ջնջել, ապա ջնջում ենք վերջինը
        ls.pop()
    for a in ls:
        ans *= 10
        ans += int(a)
    return ans


# ! TASK 16
# Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ եւ վերադարձնում նոր tuple
# բաղկացած միայն առաջին tuple֊ի թվերից։

def only_nums(t: tuple):
    ans = []
    for i in t:
        if isinstance(i, int):
            ans.append(i)
    return tuple(ans)


# ! TASK 17
# Գրեք Python ֆուկցիա որը ստանում է tuple եւ ցանկացաց տիպի օբյեկտ եւ ավելացնում 
# է ստացած արժեքը tuple մեջ։

def tuple_add(t: tuple, n):
    ls = list(t)
    ls.append(n)
    return tuple(ls)


# ! TASK 18
# Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի 
# էլեմենտները ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։

def tuple_to_string(tp):
    return '-'.join(map(str, tp))


# ! TASK 19
# Գրեք Python ֆուկցիա որը ստանում է list եւ պետքա գտնել նրա երկարությունը
# առանց len() ֆունկցիա֊ի օգտագորձմամբ։

def length(ls):
    ret = 0
    for _ in ls:
        ret += 1
    return ret


# ! TASK 20
# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky 
# if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it's lucky or not. Not using: string, list, tuple, set types.

def digit_len(n):
    ret = 0
    while n:
        n //= 10
        ret += 1
    return ret


def is_lucky(n):
    ln = digit_len(n)
    if ln % 2:
        return False
    s1, s2 = 0, 0
    for _ in range(ln // 2):
        s1 += n % 10
        n //= 10
    for _ in range(ln // 2, ln):
        s2 += n % 10
        n //= 10
    return s1 == s2


# ! TASK 21
# Euler function is return a count of numbers not great than N, which are mutualy simple with N.
# Example φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function 
# which return count of numbers mutually simple with given N.

def gcd(x, y):
    ret, small = 1, y if x > y else x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            ret = i
    return ret


def phi(n):
    if n == 1:
        return 1
    ls = []
    for i in range(1, n):
        if gcd(n, i) == 1:
            ls.append(i)
    return len(ls)


# ! TASK 22 *
# You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
# In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] 
# are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select 
# an index that satisfies the conditions.
# Return words after performing all operations. It can be shown that selecting the indices for each 
# operation in any arbitrary order will lead to the same result.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using 
# all the original letters exactly once. For example, "dacb" is an anagram of "abdc".

def rm_anagram(words):
    for i in range(len(words) - 1, 0, -1):
        if sorted(words[i]) == sorted(words[i - 1]):
            words.pop(i)
    return words


# ! TASK 23 **
# You are given an array of strings names, and an array heights that consists of distinct positive integers.
# Both arrays are of length n. For each index i, names[i] and heights[i] denote the name and height of the 
# ith person. Return names sorted in descending order by the people's heights.

def army_sort(names: list[str], heights: list[int]):
    d = dict(zip(heights, names))
    ret = []
    for i in sorted(d.keys(), reverse=True):
        ret.append(d[i])
    return ret


# ! TASK 24 ***
# In a special ranking system, each voter gives a rank from highest to lowest to all teams participating in the 
# competition.The ordering of teams is decided by who received the most position-one votes. If two or more teams
# tie in the first position, we consider the second position to resolve the conflict, if they tie again, we
# continue this process until the ties are resolved. If two or more teams are still tied after considering all
# positions, we rank them alphabetically based on their team letter.
#     You are given an array of strings votes which is the votes of all voters in the ranking systems. Sort all
# 	teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.


def vote_sort(votes):
    word_len = len(votes[0])
    d = {k: 0 for (k) in votes[0]}
    for vote in votes:
        for letter in range(word_len):
            d[vote[letter]] += 26 ** (word_len - letter)
    sorted_values = sorted(d.values(), reverse=True)
    sorted_keys = sorted(d.keys())
    s = []
    for i in sorted_values:
        for k in sorted_keys:
            if d[k] == i and k not in s:
                s.append(k)
    return ''.join(s)
