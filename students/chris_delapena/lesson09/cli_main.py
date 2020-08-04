# Chris Dela Pena
# cli_main.py

import sys
from donor_models import DonorCollection, Donor

donorcollection = DonorCollection()
donorcollection.add_donor("William Gates, III", [653772.32, 12.17])
donorcollection.add_donor("Jeff Bezos", [877.33])
donorcollection.add_donor("Paul Allen", [663.23, 43.87, 1.32])
donorcollection.add_donor("Mark Zuckerberg", [1663.23, 4300.87, 10432.0])

prompt = "\n".join(("Mail Room Program version 5.0",
            "Please choose from below options:",
            "1 - Send a Thank you",
            "2 - Send all Donors a Thank You",
            "3 - Create a Report",
            "4 - Quit",
            ">>> "))

prompt_name = "\n".join(("Please enter the full name of the donor",
                "or type 'list' to see a full list of donor names",
                "or type 'q' to quit."
                ">>> "))

prompt_amount = "\n".join(("What was the donation amount?",
                ">>> "))

def donation():
        donation_amount = input(prompt_amount)
        try:
            donation_amount = float(donation_amount)
            if donation_amount <= 0:
                print("Not a positive value")
            else:
                return donation_amount
        except ValueError:
                print("Not a dollar value")

def thank_you():
    donor_name = input(prompt_name)
    if donor_name.upper() == 'Q':
        return
    elif donor_name.upper() == "LIST":
        donorcollection.donor_list
    else:
        #if donor is found in db
        if donor_name not in donorcollection.donor_db:
            donorcollection.add_donor
        donation_amount = donation()
        donor.add_donation
        print('-'*80)
        print_thank_you(donor_name, donation_amount)
        print('-'*80)
        return

def print_thank_you(donor_name, donation_amount):
    print(f"Dear {donor_name}, thank you for your generous donation of ${donation_amount}. Regards, the Club Owners")

def thank_you_bulk():
    for i in donor_db.items():
        with open(f"{i[0]}.txt", "w") as note:
            note.write(f"Dear {i[0]}, thank you for your generous donations totaling ${sum(i[1]):.2f} \n\n Regards, the club owners")

def donor_report():
    print('-'*80)
    print('-'*80)
    header = ["Donor", "Total Donated", "Times Donated", "Average Donation"]
    print(f"{header[0]:<20}{header[1]:<15}{header[2]:<15}{header[3]:<7}")
    print('-'*80)
    #Create sorted list. use sorted(donor_db.items())
    donors_sorted = sort_donors()
    format_report(donors_sorted)
    print('-'*80)

def sort_donors():
    return sorted(donor_db.items(), key=sort_key, reverse=True)

def sort_key(donor_db):
    return donor_db[1]

def format_report(donors_sorted):
    for i in donors_sorted:
        print(f"{i[0]:<20}{sum(i[1]):<15.2f}{len(i[1]):<15}{sum(i[1])/len(i[1]):<7.2f}")

def quit():
    print("Goodbye and have a great day!")
    sys.exit()

def main():

    prompt_dict = {"1": thank_you,
                    "2": thank_you_bulk,
                    "3": donor_report,
                    "4": quit}

    while True:
        response = input(prompt)
        try:
            prompt_dict[response]()
        except KeyError:
            print("Input must be 1, 2, 3 or 4")

if __name__ == "__main__":
    main()
