*** Settings ***
Library           bank.py

*** Variables ***
${RATES}          {'BYN': {'BYN': 1.0000, 'USD': 0.3149, 'EUR': 0.2896},
...                'EUR': {'BYN': 3.4530, 'USD': 1.0872, 'EUR': 1.0000},
...                'USD': {'BYN': 3.1760, 'USD': 1.0000, 'EUR': 0.9198}}

*** Test Cases ***
Verify Conversion Between BYN and USD
    ${converter}=    Evaluate    bank.CurrencyConverter(${RATES})
    ${result}=       Evaluate    (${converter.exchange_currency('BYN', 100, 'USD')})
    Should Not Be Empty    ${result}
    Should Be Equal As Numbers    ${result}[0]    31.49

Test Client Registration
    ${bank}=    Evaluate    bank.Bank()
    ${result}=    Evaluate    '${bank.register_client('123', 'Alice')}'
    Should Be Equal    ${result}    None


Test Interest Calculation
    ${bank}=    Evaluate    bank.Bank()
    Evaluate   '${bank.register_client('123', 'Alice')}'
    Evaluate   '${bank.open_deposit_account('123', 1000, 2)}'
    ${interest}=    Evaluate    '${bank.calc_interest_rate('123')}'
    Should Be Equal As Numbers    ${interest}    1220.39

Test Closing Deposit
    ${bank}=    Evaluate    bank.Bank()
    Evaluate    '${bank.register_client('123', 'Alice')}'
    Evaluate    '${bank.open_deposit_account('123', 1000, 2)}'
    Evaluate    '${bank.calc_interest_rate('123')}'
    ${result}=    Evaluate    '${bank.close_deposit('123')}'
    Should Contain    ${result}    Client got 1220.39 money. Deposit is closed
