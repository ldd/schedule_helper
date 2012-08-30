from write_list import write_schd_info
from get_list import fetch_list

my_path = '/home/ldd/Dropbox/McGill/stuff/'
ignore_list = ['7','5','6','4','273','202','206','250','251']

fetch_list('COMP', 'SC',my_path)
fetch_list('PHIL', '', my_path)

write_schd_info(my_path, 'MT',ignore_list)
