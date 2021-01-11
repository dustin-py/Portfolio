from database_utils import connect_to_db, insert_data, create_table

table_name = 'thm_profile_badges'
column_names = [
  'badge_name', 'badge_description', 'badge_img'
]
col_d_types = [
  'VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)'
]
row_data_tuple = (
    """'Mr. Robot', 'Completing the Mr. Robot room.', 'mrrobot.svg'""",
    """'Hash Cracker', 'Cracking all those hashes', 'hashcracker.svg'""",
    """'Burp`ed', 'Completing th BurpSuite room.', 'burped.svg'""",
    """'OhSINT', 'Completing the OhSINT room', 'ohsint.svg'""",
    """'cat linux.txt', 'Being competent in Linux', 'linux.svg'""",
    """'Metasploiable', 'Contains the knowledge to use Metasploit', 'metasploit.svg'""",
    """'Ice', 'Exploiting Windows via a media server', 'ice.svg'""",
    """'Blue', 'Hacking into Windows via EternalBlue', 'blue.svg'""",
    """'Webbed', 'Understands how the world wide web works', 'webbed.svg'""",
    """'7 Day Streak', 'Achieving a 7 day hacking streak', 'streak7.svg'""",
    """'Linux PrivEsc', 'Mastering Linux Privilege Escalation', 'linuxprivesc.svg'""",
    """'OWASP Top 10', 'Understanding every OWASP vulnerability', 'owasptop10.svg'""",
    """'Overpassed', 'Completing the Overpass series', 'overpass_badge.svg'""",
)

create_table(table_name, column_names, col_d_types)
conn = connect_to_db(db='mysite')
cur = conn.cursor()
col_string = ''
for e, i in enumerate(column_names):
  if e is len(column_names)-1:
    col_string = col_string + i
  else:
    col_string = col_string + i + ', ' 
for item in row_data_tuple:   
  insert_data(table_name, col_string, item)
conn.close()
print('Database connection closed')