# combo_lock

Combination Lock¶
Making the Lock
In this exercise, we're going to get some exercise building and opening combination locks using OOP.

When we build a lock, the first thing we need to know is how many digits are in the combination. Most combination locks take between 3 and 8 digit combinations.

For now, let's assume each input digit is 0-9, although some combination locks, like the popular Master dial lock take inputs 0-39.

To open the lock, we first need to clear the lock. Then, we enter the digits one at a time. At any time, we can try to open the lock and one of two things will happen: either it will open, or not. The lock will only open when the input contains the correct number of digits and they are all correct.

Create a file combo_lock.py that contains a class ComboLock and share it with your partner. Your partner should be able to use it as follows:

    from combo_lock import ComboLock

    my_lock = ComboLock(digits = 4)
After that, they should be able to figure out how to use the lock using dir(my_lock). (No peeking at the combo!)

Opening the Lock
Now that you've recieved a lock from your partner, try opening it. How many attempts does it take to open it? Think of at least two different strategies to try opening it. Create 1000 locks and try the two different strategies. Would this be an efficient way to try a really large number of locks? How many attempts would you expect it to take using different strategies? Create plots that show the distribution of how many attempts it takes to open the locks with each strategy.
