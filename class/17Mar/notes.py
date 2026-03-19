"""
sleep(5) is not the correct way of holding the execution, the correct way is : Implicit Wait

Implicit Wait (Global Wait) because if you give it once it is marked for all find element used in script
only works for find_element/elements, it just looks for the presence of element
if element is not present -> page is still loading -> Implicit wait(15) # wait for 15 secs -> during these 15 secs it will check for in every half a second
for the element if it has arrived or not while time is getting deducted
if in 13 secs element arrives -> if element is present -> returns element
else -> time over, reached 0 secs -> returns "NoSuchElementException"

if the element is found before the time finishes then also it will return and so unlike sleep no time will be wasted and it will return automatically just
as the element is found


Explicit Wait is the same as implicit wait just the difference is that implict wait is checking only for the element if
its present inside the DOM or not and explicit wait on the other hand is waiting for the elements to do actions like it is
looking if element is actionable or not
"""