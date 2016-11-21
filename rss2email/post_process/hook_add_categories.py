from email.utils import formataddr
from email.utils import parseaddr

def process(feed, parsed, entry, guid, message):
	'''add categories at various places'''
	split = feed.name.split('.')

	message['Subject'].append(' - ' + split[0])
	to_name, to_addr = parseaddr(str(message['To']))
	mail_prefix, mail_postfix = to_addr.split('@')

	# add categories header
	# update subject with feed name and categories
	# update receiver with categories
	for category in split[1:]:
		message['X-RSS-CATEGORY'] = category
		message['Subject'].append(' [' + category + ']')
		mail_prefix = mail_prefix + '+' + category

	# update receiver field
	message.replace_header('To',formataddr((to_name, mail_prefix + '@' + mail_postfix)))

	return message
