from texts import Texts
import S_calc

if __name__ == '__main__':
    text = Texts()
    s_c = S_calc.Square_Calc()
    s_c.welcome(text.help, text.about, text.history)
