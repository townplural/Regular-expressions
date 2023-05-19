pattern_fio = r'([А-Я][а-я]+)[\s,]([А-Я][а-я]+)[\s,]([А-Яа-я]+)?'
pattern_phone = r'(8|\+7)\s?(\()?(\d+)(\))?\s?[-]?(\d{3})\s?[-]?(\d{2})\s?[-]?(\d{2})'
subst_phone = r'+7(\3)\5-\6-\7'
pattern_add_phone = r'(\()?доб. (\d+)*(\))?'
subst_add_phone = r'доб.\2'