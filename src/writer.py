from .models.term_deposit_details import TermDepositDetails


def print_result(term_deposit_details: TermDepositDetails) -> str:
    print(f"""
    Total Interest Made = ${term_deposit_details.total_interest()}
""")
