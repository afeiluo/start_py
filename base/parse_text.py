#!/usr/bin/env python
# encoding:utf-8
import re
pattern_text = u'「[\u4e00-\u9fa5|\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]+」'
a = u'您好，您在「{{ title_link }}」下的评论已被删除，原因是包含「政治敏感」内容。'
pattern = re.compile(u'「[\u4e00-\u9fa5|\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]+」')
result = re.match(pattern, a)






print re.sub(pattern_text, u'「{{reason_id}}」', a)