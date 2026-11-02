
## 1. Problem Statement

Develop a Python program to calculate parking fees based on vehicle entry and exit times. The program considers different vehicle categories, overnight parking, daily parking limits, and penalty conditions. It also validates time inputs to ensure accurate fee calculation and displays the final parking bill.

## 2. Algorithm

1. Start the program.
2. Enter vehicle number and vehicle category.
3. Enter parking entry time and exit time.
4. Validate the entered time values.
5. Calculate the total parking duration.
6. Check whether the parking is overnight.
7. Apply parking charges according to the vehicle category.
8. Calculate additional overnight charges if applicable.
9. Check the daily parking limit.
10. Apply penalty charges if the parking duration exceeds the allowed limit.
11. Calculate the total parking fee.
12. Display vehicle details, parking duration, penalties, and total fee.
13. Stop the program.

## 3. Flowchart

Copy this flowchart directly into your record.

```
              ┌───────────────┐
              │     START     │
              └───────┬───────┘
                      │
              ┌───────▼───────┐
              │ Enter Vehicle │
              │    Details    │
              └───────┬───────┘
                      │
              ┌───────▼───────┐
              │ Enter Entry   │
              │ and Exit Time │
              └───────┬───────┘
                      │
              ┌───────▼───────┐
              │ Validate Time │
              │    Inputs     │
              └───────┬───────┘
                      │
                ┌─────▼─────┐
                │ Valid Time?│
                └──┬─────┬──┘
                 No│     │Yes
            ┌──────▼─┐   │
            │ Display│   │
            │ Error  │   │
            └────┬───┘   │
                 │       ▼
                 │  ┌──────────────┐
                 │  │ Calculate    │
                 │  │ Parking Time │
                 │  └──────┬───────┘
                 │         │
                 │  ┌──────▼───────┐
                 │  │ Check Vehicle│
                 │  │   Category   │
                 │  └──────┬───────┘
                 │         │
                 │  ┌──────▼───────┐
                 │  │ Calculate    │
                 │  │ Parking Fee  │
                 │  └──────┬───────┘
                 │         │
                 │  ┌──────▼───────┐
                 │  │ Check        │
                 │  │ Overnight    │
                 │  │ Parking      │
                 │  └──────┬───────┘
                 │         │
                 │  ┌──────▼───────┐
                 │  │ Apply Daily  │
                 │  │ Limit and    │
                 │  │ Penalties    │
                 │  └──────┬───────┘
                 │         │
                 │  ┌──────▼───────┐
                 │  │ Calculate    │
                 │  │ Total Fee    │
                 │  └──────┬───────┘
                 │         │
                 │  ┌──────▼───────┐
                 │  │ Display      │
                 │  │ Parking Bill │
                 │  └──────┬───────┘
                 │         │
                 │  ┌──────▼───────┐
                 │  │     STOP     │
                 │  └──────────────┘
                 │
                 └──> Re-enter Time
```

## 4. Sample Input

```
Enter Vehicle Number: AP39AB1234

Vehicle Category: Car

Enter Entry Time (HH:MM): 09:00

Enter Exit Time (HH:MM): 18:00

Overnight Parking: No

Daily Parking Limit: Rs. 200

Penalty: Rs. 50
```

## 5. Sample Output

```

Vehicle Number       : AP39AB1234
Vehicle Category     : Car
Entry Time           : 09:00
Exit Time            : 18:00

Parking Duration     : 9 Hours
Parking Charge       : Rs. 90
Overnight Charge     : Rs. 0
Penalty              : Rs. 0

Total Parking Fee    : Rs. 90


       
