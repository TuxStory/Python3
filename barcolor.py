import numpy as np
import matplotlib.pyplot as plt
 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
bar = plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
bar[1].set_color('red')
bar[2].set_color('g')
bar[3].set_color('y')
bar[4].set_color('purple')
bar[5].set_color('grey')
plt.ylabel('Usage')
plt.title('Programming language usage')
bar[0].set_label('Python')
bar[1].set_label('C++')
bar[2].set_label('Java')
bar[3].set_label('Perl')
bar[4].set_label('Scala')
bar[5].set_label('Lisp')
plt.legend()
plt.grid()
 
plt.show()