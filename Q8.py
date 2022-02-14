#Q8. wap to perform various set operations on the given set of numbers

set1={1, 2, 3, 4, 5}
set2={2, 4, 6, 8}
set3={1, 5, 9, 13, 17}
int_10={1,2,3,4,5,6,7,8,9,10}


print('Part A) -> ',(set1|set2)-(set1&set2))
print('Part B) -> ',(set1|set2|set3)-((set1&set2)|(set1&set3)|(set3&set2)))
print('Part C) -> ',((set1&set2)|(set1&set3)|(set3&set2))-(set1&set2&set3))
print('Part D) -> ',int_10-set1)
print('Part E) -> ',int_10-(set1|set2|set3))
