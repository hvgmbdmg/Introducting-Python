import module.first.fun1st as f1
import module.Chapter2.c2 as c2
import module.Chapter3.c3 as c3


# page 3 -- dictionary {key : value}
quotes = {
"Moe": "A wiseguy, huh?",
"Larry": "Ow!",
"Curly": "Nyuk nyuk!"
}

stooge = "Curly"
print(stooge, "says:", quotes[stooge])


f1.fun1()
#f1.fun2()

c2.introduction()
c2.test_operator()
c2.test_base()
c2.test_str()
c2.test_characters()
c2.test_split_join()
c2.test_str_long()
c2.test_align()
c2.test_replace()


c3.introduction()