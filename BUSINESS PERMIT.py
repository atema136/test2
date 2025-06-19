
import datetime

class BusinessPermitApplication:
    def __init__(self):
        self.applicant_name = ""
        self.business_name = ""
        self.business_type = ""
        self.location = ""
        self.phone = ""
        self.id_number = ""
        self.documents_submitted = {
            "Application Form": False,
            "Valid ID": False,
            "Business Plan": False
        }
        self.submission_date = None
        self.verified = False
        self.payment_done = False
        self.payment_receipt = ""
        self.inspection_report = {}
        self.approved = False
        self.permit_issued = False

    # Step 1: Application & Submission
    def apply(self):
        print("\n📥 Step 1: Application & Document Submission")
        self.applicant_name = input("Applicant Full Name: ")
        self.business_name = input("Business Name: ")
        self.business_type = input("Business Type (Retail/Service/Other): ")
        self.location = input("Business Location (Town/Ward): ")
        self.phone = input("Phone Number: ")
        self.id_number = input("ID Number: ")

        print("\n📎 Submit Required Documents (yes/no):")
        for doc in self.documents_submitted:
            response = input(f"{doc}: ").strip().lower()
            self.documents_submitted[doc] = (response == "yes")

        if all(self.documents_submitted.values()):
            self.submission_date = datetime.date.today()
            print(f"\n✅ Application received on {self.submission_date}.")
        else:
            print("\n❌ Application incomplete. Please submit all required documents.")
            return False
        return True

    # Step 2: Document Review
    def review_documents(self):
        print("\n🧐 Step 2: Document Review by Permit Officer")
        if all(self.documents_submitted.values()):
            self.verified = True
            print("✅ All documents verified and accepted.")
        else:
            print("❌ Missing documents. Cannot proceed.")
            self.verified = False
        return self.verified

    # Step 3: Payment
    def make_payment(self):
        print("\n💰 Step 3: Payment of Business Fee")
        if not self.verified:
            print("❌ Cannot pay before document verification.")
            return False
        try:
            amount = float(input("Enter assessment fee amount (KES): "))
            self.payment_receipt = input("Enter official receipt number: ")
            self.payment_done = True
            print(f"✅ Payment of KES {amount} received. Receipt: {self.payment_receipt}")
            return True
        except ValueError:
            print("1000-50000.")
            return False

    # Step 4: Inspection
    def inspection(self):
        print("\n🛠 Step 4: Inspection & Evaluation")
        if not self.payment_done:
            print("❌ Cannot inspect before payment.")
            return False
        self.inspection_report["Site Location Confirmed"] = input("Site location confirmed? (yes/no): ") == "yes"
        self.inspection_report["Safety Compliance"] = input("Safety compliance confirmed? (yes/no): ") == "yes"
        self.inspection_report["Documents On-Site"] = input("Documents present at site? (yes/no): ") == "yes"

        passed = all(self.inspection_report.values())
        if passed:
            print("✅ Inspection passed.")
        else:
            print("❌ Inspection failed. Fix issues before approval.")
        return passed

    # Step 5: Approval
    def approve(self):
        print("\n✔️ Step 5: Approval by Permit Authority")
        if not all(self.inspection_report.values()):
            print("❌ Incomplete inspection. Cannot approve.")
            return False
        self.approved = True
        print("✅ Application approved.")
        return True

    # Step 6: Permit Issuance
    def issue_permit(self):
        print("\n📄 Step 6: Permit Issuance")
        if self.approved:
            self.permit_issued = True
            print(f"\n🎉 Official Business Permit Issued to {self.business_name} on {datetime.date.today()}.")
            return True
        else:
            print("❌ Application not approved yet.")
            return False


def main():
    print("🏛 Kakamega County Business Permit Issuance System")
    app = BusinessPermitApplication()

    if not app.apply():
        return
    input("\nPress Enter to proceed to Step 2: Review...")
    if not app.review_documents():
        return
    input("\nPress Enter to proceed to Step 3: Payment...")
    if not app.make_payment():
        return
    input("\nPress Enter to proceed to Step 4: Inspection...")
    if not app.inspection():
        return
    input("\nPress Enter to proceed to Step 5: Approval...")
    if not app.approve():
        return
    input("\nPress Enter to proceed to Step 6: Permit Issuance...")
    app.issue_permit()

if __name__ == "__main__":
    main()
