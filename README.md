UK Area code crawler
-------------

The **UK Area code crawler** crawls [area-codes.org.uk](http://area-codes.org.uk)  for the list of UK codes.

We start with checking if there are any policy limits on crawlers or request frequency for that specific website by looking up the website's [robots.txt](http://www.area-codes.org.uk/robots.txt). It seems that in our case there is none.

The primary crawler is in `crawler.py`:
```
   python crawler.py
```
The script uses `requests` library, we may need to install it:
```
   pip install requests
```
The output is a csv file in the following format:
```
   0115,Nottingham,7
```
Here `0115` is the area code, Nottingham is the area's toponim and 7 is the number of digits in the local phone numbers.

There is a special case when for some area codes, the number of digits in the number varies. As no comment was given on how to treat these cases, the first mentioned of the possible options was taken. For example, for the case when it is stated on the page that:
```
    Local telephone numbers in Wigton are five or six digits long.
```
the resultant line was
```
    016973,Wigton,5
```
Whenever something went wrong and we had a special case, the corresponding coment was written that contained the key word: 'Not found'.

These special cases are filtered out with filter_not_fixed.py:
```
    python filter_not_fixed.py
```
It yeilds only one special case: combined 016977 and 01697 area codes for the city of Brampton. Since it is only two cases I fixed them by hand.

More generally, the list of special cases can be addressed in the future and then introduced into the primary results with `joiner.py` script.
```
    python joiner.py
```
The final CSV file is in `out_final.csv`.