from projectapi.viewsets import ProjectViewset
from userapi.viewsets import UserViewset
from issueapi.viewsets import IssueViewset
from typeapi.viewsets import TypeViewset
from statusapi.viewsets import StatusViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('project', ProjectViewset)
router.register('issue', IssueViewset)
router.register('user', UserViewset)
router.register('type', TypeViewset)
router.register('status', StatusViewset)
#router.register('type', TypeViewset)

