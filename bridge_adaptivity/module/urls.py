from django.conf.urls import url
from django.urls import reverse_lazy
from django.views.generic import RedirectView

from module.views import (
    ActivityCreate, ActivityDelete, ActivityUpdate, AddCollectionInGroup, callback_sequence_item_grade,
    CollectionCreate, CollectionDelete, CollectionDetail, CollectionGroupDelete, CollectionList, CollectionOrderAdd,
    CollectionOrderUpdate, CollectionUpdate, CourseAddGroup, CourseCreate, CourseDelete, CourseDetail, CourseList,
    CourseRmGroup, CourseUpdate, demo_collection, GetCollectionForm, GetGradingPolicyForm, GroupCreate, GroupDelete,
    GroupDetail, GroupList, GroupUpdate, preview_collection, sequence_item_next, SequenceComplete, SequenceDelete,
    SequenceItemDetail, sync_collection, update_students_grades
)

urlpatterns = ([
    url(r'^course/$', CourseList.as_view(), name='course-list'),
    url(r'^course/add/?$', CourseCreate.as_view(), name='course-add'),
    url(r'^course/(?P<course_slug>[\w-]+)/$', CourseDetail.as_view(), name='course-detail'),
    url(r'^course/(?P<course_slug>[\w-]+)/change/?$', CourseUpdate.as_view(), name='course-change'),
    url(r'^course/(?P<course_slug>[\w-]+)/delete/?$', CourseDelete.as_view(), name='course-delete'),
    url(r'^course/(?P<course_slug>[\w-]+)/add_group/?$', CourseAddGroup.as_view(), name='add-group-to-course'),
    url(r'^course/(?P<course_slug>[\w-]+)/rm_group/(?P<group_id>[\w-]+)?/?$', CourseRmGroup.as_view(),
        name='rm-group-from-course'),

    url(r'^group/$', GroupList.as_view(), name='group-list'),
    url(r'^(?:course/(?P<course_slug>[\w-]+)/)?group/add/?$', GroupCreate.as_view(), name='group-add'),
    url(r'^group/(?P<group_id>[\w-]+)/$', GroupDetail.as_view(), name='group-detail'),
    url(r'^group/(?P<group_id>[\w-]+)/change/?$', GroupUpdate.as_view(), name='group-change'),
    url(r'^group/(?P<group_id>[\w-]+)/delete/?$', GroupDelete.as_view(), name='group-delete'),
    url(r'^group/(?P<group_id>[\w-]+)/add_collection/?$', AddCollectionInGroup.as_view(),
        name='add-collection-to-group'),
    url(r'^collection_order/(?P<collection_order_slug>[\w-]+)/delete/', CollectionGroupDelete.as_view(),
        name='collection-group-delete'),
    url(
        r'collection_order/(?:(?P<collection_order_slug>[\w-]+))?/grading_policy_form/?$',
        GetGradingPolicyForm.as_view(),
        name='grading_policy_form'
    ),
    url(r'collection/collection_form/$', GetCollectionForm.as_view(), name='collection_form'),
    url(r'^(?:group/(?P<group_id>\d+)/)?collection/$', CollectionList.as_view(), name='collection-list'),
    url(r'^(?:group/(?P<group_id>\d+)/)?collection/add/$', CollectionCreate.as_view(),
        name='collection-add'),
    url(r'collection/(?P<pk>\d+)/change/', CollectionUpdate.as_view(), name='collection-change'),
    url(
        r'collection_order/(?P<collection_order_slug>[\w-]+)/change$',
        CollectionOrderUpdate.as_view(),
        name='collection-order-change'
    ),
    url(
        r'group/(?P<group_id>\d+)/add/collection_order/$', CollectionOrderAdd.as_view(), name='collection-order-add'
    ),
    url(
        r'^(?:group/(?P<group_id>\d+)/)?collection/(?P<pk>\d+)/$',
        CollectionDetail.as_view(),
        name='collection-detail'
    ),
    url(
        r'^(?:group/(?P<group_id>\d+)/)?collection/(?P<pk>\d+)/delete/?$',
        CollectionDelete.as_view(),
        name='collection-delete'
    ),
    url(
        r'collection_order/(?P<collection_order_slug>[\w-]+)/demo',
        demo_collection,
        name="demo"
    ),
    url(r'sequence/(?P<pk>\d+)', SequenceDelete.as_view(), name="delete_sequence"),
    url(
        r'^collection_order/(?P<collection_order_slug>[\w-]+)/move/(?P<order>\d+)?$',
        GroupUpdate.as_view(),
        name='collection-move'
    ),
    url(r'^activity/(?P<collection_id>\d+)/add/$', ActivityCreate.as_view(), name='activity-add'),
    url(
        r'^activity/(?P<pk>\d+)/(?P<collection_id>\d+)/change/$',
        ActivityUpdate.as_view(),
        name='activity-change'
    ),
    url(
        r'^activity/(?P<pk>\d+)/move/(?P<order>\d+)?$',
        ActivityUpdate.as_view(),
        name='activity-move'
    ),
    url(
        r'^activity/(?P<pk>\d+)/delete/$',
        ActivityDelete.as_view(),
        name='activity-delete'
    ),
    url(
        r'^sequence_item/(?P<pk>\d+)/$',
        SequenceItemDetail.as_view(),
        name='sequence-item'
    ),
    url(
        r'^sequence_item/(?P<pk>\d+)/next/$',
        sequence_item_next,
        name='sequence-item-next'
    ),
    url(r'^sequence_complete/(?P<pk>\d+)/$', SequenceComplete.as_view(), name='sequence-complete'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('module:collection-list'))),

    # Source outcome service endpoint
    url(r'^callback_grade/$', callback_sequence_item_grade, name='sequence-item-grade'),

    # Sync collection with relative engines
    url(r'^collection/(?P<pk>\d+)/sync/$', sync_collection, name='collection-sync'),

    # Manually update students grades related to the collection-group
    url(
        r'collection_order/(?P<collection_order_slug>[\w-]+)/update_grades/',
        update_students_grades,
        name='update_grades'
    ),

    url(r'collection/(?P<pk>\d+)/preview/', preview_collection, name='collection-preview'),
], 'module')
