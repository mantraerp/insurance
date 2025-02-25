# Copyright (c) 2025, Mantra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_days, getdate, formatdate


class Policy(Document):
    pass
    
@frappe.whitelist()
def check_and_send_reminders():
    """Check all policies and send email reminders if the reminder date matches today's date"""
    
    policies = frappe.get_all('Policy',fields=['*'])

    today_date = getdate()

    for policy in policies:
        if policy.renew:  
            return
        
        period_to = getdate(policy.period_to)
       
        if policy.reminder_1 and policy.reminder1_before_days:  
            reminder1_date = getdate(add_days(period_to, -policy.reminder1_before_days + 1))  
            if reminder1_date == today_date:  
                send_reminder_email(policy.name)
                
        if policy.reminder_2 and policy.reminder2_before_days:  
            reminder2_date = getdate(add_days(period_to, -policy.reminder2_before_days + 1))  
            if reminder2_date == today_date:  
                send_reminder_email(policy.name)  
              
        if policy.reminder_3 and policy.reminder3_before_days:  
            reminder3_date = getdate(add_days(period_to, -policy.reminder3_before_days + 1))  
            if reminder3_date == today_date:  
                send_reminder_email(policy.name)
                 
                
def send_reminder_email(name):
    """Send reminder email to the recipients"""
    
    policy = frappe.get_doc('Policy', name) 

    email_addresses = []

    
    for recipient in policy.recipients:
        email_addresses.append(recipient.recipients)

    if not email_addresses:
        frappe.log_error(f"No valid emails for Policy {policy.name}", "Email Error Log")

    period_to_formatted = formatdate(policy.period_to, "dd-mm-yyyy")
    
    subject = f"Reminder: Insurance policy {policy.name} is about to expire"
    message = f"""
    <h3>Insurance Policy Reminder</h3>
    <p>This is a reminder that your insurance policy <b>{policy.name}</b> is expire on <b>{period_to_formatted}</b>.</p>
    """
    
    send_email(email_addresses, subject, message)

def send_email(email_addresses, subject, message):
    """Function to send email to multiple recipients"""
    try:
        frappe.sendmail(
            recipients=email_addresses,
            subject=subject,
            message=message,
            now=True
        )
    except Exception as e:
        error_message = f"Failed to send email to {email_addresses}: {str(e)}"
        frappe.log_error(error_message, "Email Error Log")