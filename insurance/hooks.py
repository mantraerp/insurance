app_name = "insurance"
app_title = "Insurance"
app_publisher = "Mantra"
app_description = "To mange insurance reminder"
app_email = "ravi.patel@mantratec.com"
app_license = "mit"


# Scheduled Tasks
# ---------------

scheduler_events = {

	"daily": [
        "insurance.insurance.doctype.policy.policy.check_and_send_reminders"
    ],
}
