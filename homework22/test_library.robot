*** Settings ***
Library    library.py

*** Variables ***
${TITLE}          The Great Gatsby
${AUTHOR}         F. Scott Fitzgerald
${NUM_PAGES}      180
${ISBN}           9783161484100

*** Keywords ***
Create Book Instance
    ${book}=    Evaluate     library.Book("${TITLE}", "${AUTHOR}", "${NUM_PAGES}", "${ISBN}")
    RETURN    ${book}
Reserve Book
    [Arguments]    ${book}
    ${res}=    Evaluate    '${book.reserve()}'
    RETURN    ${res}

Cancel Reserve Book
    [Arguments]    ${book}
    ${result}=    Evaluate    '${book.cancel_reserve()}'
    RETURN    ${result}

Get Book
    [Arguments]    ${book}
    ${result}=    Evaluate    '${book.get_book()}'
    RETURN    ${result}

Return Book
    [Arguments]    ${book}
    ${result}=    Evaluate    '${book.return_book()}'
    RETURN    ${result}

*** Test Cases ***
Test Reserving an Available Book
    ${book}=         Create Book Instance
    ${message}=      Reserve Book    ${book}
    ${status}=       Evaluate    '${book.status}'
    Should Be Equal    ${status}    booked
    Should Be Equal As Strings    '${message}'    '${TITLE} by ${AUTHOR} is successfully booked'

Test Reserving an Already Booked Book
    ${book}=         Create Book Instance
    ${first_message}=    Reserve Book    ${book}
    ${second_message}=   Reserve Book    ${book}
    ${status}=       Evaluate    '${book.status}'
    Should Be Equal    ${status}    booked
    Should Be Equal     ${second_message}     None

Test Canceling a Reservation When Book is Booked
    ${book}=         Create Book Instance
    Reserve Book     ${book}
    ${message}=      Cancel Reserve Book    ${book}
    ${status}=       Evaluate    '${book.status}'
    Should Be Equal    ${status}    available
    Should Be Equal    ${message}    Your booking was successfully cancelled

Test Canceling a Reservation When Book is Not Booked
    ${book}=         Create Book Instance
    ${message}=      Cancel Reserve Book    ${book}
    Should Be Equal    ${message}    None

Test Borrowing a Book from Available Status
    ${book}=         Create Book Instance
    ${message}=      Get Book    ${book}
    ${status}=       Evaluate    '${book.status}'
    Should Be Equal    ${status}    borrowed
    Should Be Equal    ${message}    User got the book

Test Borrowing a Book from Booked Status
    ${book}=         Create Book Instance
    Reserve Book     ${book}
    ${message}=      Get Book    ${book}
    ${status}=       Evaluate    '${book.status}'
    Should Be Equal    ${status}    borrowed
    Should Be Equal    ${message}    User got the book

Test Borrowing a Book When Already Borrowed
    ${book}=         Create Book Instance
    Get Book         ${book}
    ${message}=      Get Book    ${book}
    ${status}=       Evaluate    '${book.status}'
    Should Be Equal    ${status}    borrowed
    Should Be Equal     ${message}    None

Test Returning a Borrowed Book
    ${book}=         Create Book Instance
    Reserve Book     ${book}
    Get Book         ${book}
    ${message}=      Return Book    ${book}
    ${status}=       Evaluate    '${book.status}'
    Should Be Equal    ${status}    available
    Should Be Equal As Strings    ${message}    ${TITLE} by ${AUTHOR} is available now

Test Returning a Book When Not Borrowed
    ${book}=         Create Book Instance
    ${message}=      Return Book    ${book}
    Should Be Equal    ${message}    None
