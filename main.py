from src.generator import Generator

par = '''Margaret Abbott (June 15, 1878 – June 10, 1955) was an American amateur golfer and the first woman to win an Olympic event for the United States: the women's golf tournament at the 1900 Summer Olympics. Born in Calcutta in 1878, Abbott moved with her family to Chicago in 1884. She joined the Chicago Golf Club in Wheaton, Illinois, where she was coached by Charles B. Macdonald and H. J. Whigham. In 1899, she traveled with her mother to Paris to study art. The following year, along with her mother, she signed up for a women's golf tournament without realizing it was part of the second modern Olympics. Abbott won with a score of 47 strokes and was awarded a porcelain bowl; her mother tied for seventh. In December 1902, she married the writer Finley Peter Dunne. They moved to New York and had four children. Abbott died never realizing she won an Olympic event. She was not well known until University of Florida professor Paula Welch researched her life.'''

generator = Generator(par=par, type='sentence')

res = generator.generate()
print(res)
