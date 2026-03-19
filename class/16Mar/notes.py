"""
X path is a way of accessing any particular element like
<div>
    <input>
<div>
Traversing is of two types
1. forward -> from parent to child. can be accessed using / or //
2. backward -> from child to parent like input to div. eg : //input/..

Steps : 
1. identify static element
2. from static element move to a common parent of both static and dynamic
3. from common parent fetch dynamic element

Siblings Locator:
1. following sibling -> the below ones are
2. preceding sibling -> the above ones

<tr>
    <td> U/A </td>
    <td> Dhurandhar </td>
    <td> **** </td>
    <td> 10CR </td>
<tr>


//td[text='Dhurandhar']//following-sibling::td[2]
//td[text='Dhurandhar']//preceding-sibling::td[1]
"""