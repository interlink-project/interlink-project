from sheets import service, sheet_id
from datetime import datetime
import dateutil.relativedelta
from common import *
import json

# date in the left cell
date_time = datetime.now()
str_date = date_time.strftime("%Y-%m-%d %H:%M:%S")

d2 = date_time - dateutil.relativedelta.relativedelta(months=1)
one_month_before = d2.strftime("%Y-%m-%d")

login()

queries = [
    # interlinkers
    {
        "name": "A1: Number of interlinkers",
        "sql": "SELECT COUNT(DISTINCT(interlinker.id)) FROM catalogue.public.interlinker",
        "extract_count": True
    },
    {
        "name": "A1.1: Number of software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(softwareinterlinker.id)) FROM catalogue.public.softwareinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.2: Number of used software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(softwareinterlinker_id)) FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET'",
        "extract_count": True
    },
    {
        "name": "A1.3: Used software interlinkers",
        "sql": "SELECT softwareinterlinker_name as NAME, COUNT(softwareinterlinker_name) as TOTAL_INSTANTIATIONS, COUNT(DISTINCT(coproductionprocess_id)) AS IN_COPRODUCTION_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' GROUP BY softwareinterlinker_name",
    },
    {
        "name": "A1.4: Number of external software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(externalsoftwareinterlinker.id)) FROM catalogue.public.externalsoftwareinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.5: Number of used external software interlinkers",
        "sql": "SELECT COUNT(DISTINCT(softwareinterlinker_id)) FROM elastic2.logs.log AS logs INNER JOIN catalogue.public.externalsoftwareinterlinker AS catalogue ON logs.softwareinterlinker_id = catalogue.id WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' AND softwareinterlinker_name IS NOT null",
        "extract_count": True
    },
    {
        "name": "A1.6: Number of knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(knowledgeinterlinker.id)) FROM catalogue.public.knowledgeinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.7: Number of used knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(knowledgeinterlinker_id)) FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' AND knowledgeinterlinker_name IS NOT null",
        "extract_count": True
    },
    {
        "name": "A1.8: Used knowledge interlinkers",
        "sql": "SELECT knowledgeinterlinker_name as NAME, COUNT(knowledgeinterlinker_name) as TOTAL_INSTANTIATIONS, COUNT(DISTINCT(coproductionprocess_id)) AS IN_COPRODUCTION_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' AND knowledgeinterlinker_name IS NOT null GROUP BY knowledgeinterlinker_name",
    },
    {
        "name": "A1.9: Number of external knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(externalknowledgeinterlinker.id)) FROM catalogue.public.externalknowledgeinterlinker",
        "extract_count": True
    },
    {
        "name": "A1.10: Number of used external knowledge interlinkers",
        "sql": "SELECT COUNT(DISTINCT(knowledgeinterlinker_id)) FROM elastic2.logs.log AS logs INNER JOIN catalogue.public.externalknowledgeinterlinker AS catalogue ON logs.knowledgeinterlinker_id = catalogue.id WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' AND knowledgeinterlinker_name IS NOT null",
        "extract_count": True
    },
    # Users
    {
        "name": "A2: Number of users involved in service customization",
        "sql": "SELECT COUNT(DISTINCT(nested.user_id)) FROM (SELECT permission.coproductionprocess_id AS coproductionprocess_id, U.id as user_id FROM coproduction.public.\"user\" AS U INNER JOIN coproduction.public.\"association_user_team\" AS association_u_t ON U.id = association_u_t.user_id INNER JOIN coproduction.public.permission AS permission ON permission.team_id = association_u_t.team_id INNER JOIN coproduction.public.coproductionprocess AS coproductionprocess ON coproductionprocess.id = permission.coproductionprocess_id) nested",
        "extract_count": True
    },
    {
        "name": "A2.2. Number of users involved in co-delivered services",
        "sql": "SELECT COUNT(DISTINCT(nested.user_id)) FROM (SELECT permission.coproductionprocess_id AS coproductionprocess_id, U.id as user_id FROM coproduction.public.\"user\" AS U INNER JOIN coproduction.public.\"association_user_team\" AS association_u_t ON U.id = association_u_t.user_id INNER JOIN coproduction.public.permission AS permission ON permission.team_id = association_u_t.team_id INNER JOIN coproduction.public.coproductionprocess AS coproductionprocess ON coproductionprocess.id = permission.coproductionprocess_id) nested INNER JOIN coproduction.public.phase as phase ON nested.coproductionprocess_id = phase.coproductionprocess_id WHERE is_part_of_codelivery = 'true'",
        "extract_count": True
    },
    {
        "name": "A3: Number of INTERLINKERs used with flag is_sustainabilty related",
        "sql": "SELECT COUNT(*) FROM elastic2.logs.log WHERE softwareinterlinker_id IN (SELECT id FROM catalogue.public.interlinker WHERE interlinker.is_sustainability_related='true') OR knowledgeinterlinker_id IN (SELECT id FROM catalogue.public.interlinker WHERE interlinker.is_sustainability_related='true')",
        "extract_count": True
    },
    {
        "name": "A4: Number of users registered to INTERLINK platform",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\"",
        "extract_count": True
    },
    {
        "name": "A5: Number of users of INTERLINK enablers",
        "sql": "SELECT COUNT(DISTINCT(asset.creator_id)) from coproduction.public.asset WHERE type = 'internalasset'",
        "extract_count": True
    },
    {
        "name": "A6: Number of useres users involved in co-delivered services",
        "sql": "SELECT COUNT(DISTINCT(association.user_id)) FROM coproduction.public.\"association_user_team\" AS association INNER JOIN coproduction.public.team ON team.id = association.team_id AND team.id IN (SELECT permission.team_id FROM coproduction.public.permission INNER JOIN coproduction.public.phase ON phase.coproductionprocess_id = permission.coproductionprocess_id AND phase.is_part_of_codelivery='true')",
        "extract_count": True
    },
    {
        "name": "A6.1: Number of users involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id)",
        "extract_count": True
    },
    {
        "name": "A6.2: Number of citizens",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'citizen' )",
        "extract_count": True
    },
    {
        "name": "A6.3: Number of citizens involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen' )",
        "extract_count": True
    },
    {
        "name": "A6.4: Number of public servants",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE 'public_administration' )",
        "extract_count": True
    },
    {
        "name": "A6.5: Number of public servants involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration' )",
        "extract_count": True
    },
    {
        "name": "A6.6: Number of TSO users",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT coproduction.public.team.id FROM coproduction.public.team WHERE team.type LIKE '%organization%' )",
        "extract_count": True
    },
    {
        "name": "A6.7: Number of TSO users involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\" INNER JOIN coproduction.public.association_user_team ON coproduction.public.\"user\".id = coproduction.public.association_user_team.user_id AND coproduction.public.association_user_team.team_id IN ( SELECT team.id FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%' )",
        "extract_count": True
    },
    {
        "name": "A7: Number of TSO teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%'",
        "extract_count": True
    },
    {
        "name": "A7.1: Number of teams",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team",
        "extract_count": True
    },
    {
        "name": "A7.2: Number of public administration teams",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team WHERE team.type LIKE 'public_administration'",
        "extract_count": True
    },
    {
        "name": "A7.3: Number of public administration teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'public_administration'",
        "extract_count": True
    },
    {
        "name": "A7.4: Number of public administration teams involved in a co-delivered processes",
        "sql": "SELECT COUNT(DISTINCT(organization.id)) FROM coproduction.public.organization INNER JOIN coproduction.public.team ON team.organization_id = organization.id AND team.type LIKE 'public_administration' AND team.id IN (SELECT permission.team_id FROM coproduction.public.permission INNER JOIN coproduction.public.phase ON phase.coproductionprocess_id = permission.coproductionprocess_id AND phase.is_part_of_codelivery='true' )",
        "extract_count": True
    },
    {
        "name": "A7.5: Number of citizen teams",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team WHERE team.type LIKE 'citizen'",
        "extract_count": True
    },
    {
        "name": "A7.6: Number of citizen teams involved in a coproductionprocess",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE 'citizen'",
        "extract_count": True
    },
    {
        "name": "A7.7: Number of citizen teams involved in a co-delivered processes",
        "sql": "SELECT COUNT(DISTINCT(organization.id)) FROM coproduction.public.organization INNER JOIN coproduction.public.team ON team.organization_id = organization.id AND team.type LIKE 'citizen' AND team.id IN (SELECT permission.team_id FROM coproduction.public.permission INNER JOIN coproduction.public.phase ON phase.coproductionprocess_id = permission.coproductionprocess_id AND phase.is_part_of_codelivery='true' )",
        "extract_count": True
    },
    {
        "name": "A7.8: Number of TSO teams",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team WHERE team.type LIKE '%organization%'",
        "extract_count": True
    },
    {
        "name": "A7.9: Number of TSO teams involved in a co-production processes",
        "sql": "SELECT COUNT(DISTINCT(team.id)) FROM coproduction.public.team INNER JOIN coproduction.public.permission ON permission.team_id = team.id AND team.type LIKE '%organization%'",
        "extract_count": True
    },
    {
        "name": "A7.10: Number of TSO teams involved in a co-delivered processes",
        "sql": "SELECT COUNT(DISTINCT(organization.id)) FROM coproduction.public.organization INNER JOIN coproduction.public.team ON team.organization_id = organization.id AND team.type LIKE '%organization%' AND team.id IN (SELECT permission.team_id FROM coproduction.public.permission INNER JOIN coproduction.public.phase ON phase.coproductionprocess_id = permission.coproductionprocess_id AND phase.is_part_of_codelivery='true' )",
        "extract_count": True
    },
    {
        "name": "A8: Number of new co-delivered processes",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.id IN (SELECT coproductionprocess_id FROM coproduction.public.phase WHERE is_part_of_codelivery='true')",
        "extract_count": True
    },
    {
        "name": "A8.1: Number of new co-produced processes",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess",
        "extract_count": True
    },
    {
        "name": "A8.2: Number of coproduction processes in english",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'en'",
        "extract_count": True
    },
    {
        "name": "A8.3: Number of coproduction processes in latvian",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'lv'",
        "extract_count": True
    },
    {
        "name": "A8.4: Number of coproduction processes in italian",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'it'",
        "extract_count": True
    },
    {
        "name": "A8.5: Number of coproduction processes in spanish",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess.id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.\"language\" LIKE 'es'",
        "extract_count": True
    },
    {
        "name": "A9: Number of active users per co-produced service per month",
        "sql": "SELECT SUM(users) FROM(SELECT COUNT(DISTINCT(user_id)) AS users FROM coproduction.public.coproductionprocessnotification)",
        "extract_count": True
    },
    {
        "name": "A10: Number of shared services between PAs and citizens that were co-produced through INTERLINK platform",
        "sql": "SELECT COUNT(id) FROM(SELECT id, count(type) as type from (SELECT coprod.id, team.type FROM coproduction.public.coproductionprocess AS coprod INNER JOIN coproduction.public.permission AS permission ON permission.coproductionprocess_id = coprod.id INNER JOIN coproduction.public.team AS team ON team.id = permission.team_id GROUP BY coprod.id, team.type HAVING team.type = 'public_administration' OR team.type = 'citizen') GROUP BY id having type > 1)",
        "extract_count": True
    },
    {
        "name": "A11. Number of private companies involved in co-delivered services",
        "sql": "SELECT COUNT(DISTINCT(organization.id)) FROM coproduction.public.organization INNER JOIN coproduction.public.team ON team.organization_id = organization.id AND team.type LIKE '%organization%' AND team.id IN (SELECT permission.team_id FROM coproduction.public.permission INNER JOIN coproduction.public.phase ON phase.coproductionprocess_id = permission.coproductionprocess_id AND phase.is_part_of_codelivery='true' )",
        "extract_count": True
    },
    {
        "name": "A12: Number of shared services between PAs and private companies that were co-produced through INTERLINK platform",
        "sql": "SELECT COUNT(id) FROM(SELECT id, count(type) as type from (SELECT coprod.id, team.type FROM coproduction.public.coproductionprocess AS coprod INNER JOIN coproduction.public.permission AS permission ON permission.coproductionprocess_id = coprod.id INNER JOIN coproduction.public.team AS team ON team.id = permission.team_id GROUP BY coprod.id, team.type HAVING team.type = 'public_administration' OR team.type = 'citizen') GROUP BY id having type > 1)",
        "extract_count": True
    },
    {
        "name": "A12.2. Number of public services that have cloned or derived from existing public services",
        "sql": "SELECT COUNT(DISTINCT(id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.cloned_from_id IS NOT NULL",
        "extract_count": True
    },
    {
        "name": "A12.3: List processes with teams with more than 1 user type indicating types of teams for each",
        "sql": "SELECT copro.id, COUNT(DISTINCT(team.type)) AS num_teams from coproduction.public.coproductionprocess AS copro INNER JOIN coproduction.public.permission AS permission ON permission.coproductionprocess_id = copro.id INNER JOIN coproduction.public.team AS team ON team.id = permission.team_id GROUP BY copro.id HAVING COUNT(DISTINCT(team.type)) > 1",
    },
    {
        "name": "A13: Number of coproduction processes involved in sustainability",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocess_id)) FROM ( SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.internalasset ON asset.id = internalasset.id WHERE knowledgeinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) UNION ALL SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.internalasset ON asset.id = internalasset.id WHERE softwareinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) UNION ALL SELECT coproductionprocess_id FROM Coproduction.public.asset INNER JOIN Coproduction.public.externalasset ON asset.id = externalasset.id WHERE externalinterlinker_id in ( SELECT id FROM catalogue.public.interlinker WHERE is_sustainability_related = True ) )",
        "extract_count": True
    },
    {
        "name": "A16: Number of interlinkers reused in more than one coproduction process",
        "sql": "SELECT COUNT(*) FROM( SELECT knowledgeinterlinker_name, softwareinterlinker_name, COUNT(DISTINCT(coproductionprocess_id)) AS IN_PROCESSES FROM elastic2.logs.log WHERE action LIKE 'CREATE' AND model LIKE 'ASSET' GROUP BY knowledgeinterlinker_name, softwareinterlinker_name ) WHERE IN_PROCESSES > 1",
        "extract_count": True
    },
    {
        "name": "A17: Number of resources",
        "sql": "SELECT COUNT(DISTINCT(asset.id)) FROM coproduction.public.asset",
        "extract_count": True
    },
    {
        "name": "A18: Number of external resources",
        "sql": "SELECT COUNT(DISTINCT(externalasset.id)) FROM coproduction.public.externalasset",
        "extract_count": True
    },
    {
        "name": "A19: Number of internal resources",
        "sql": "SELECT COUNT(DISTINCT(internalasset.id)) FROM coproduction.public.internalasset",
        "extract_count": True
    },
    {
        "name": "A20: Number of organizations",
        "sql": "SELECT COUNT(DISTINCT(organization.id)) FROM coproduction.public.organization",
        "extract_count": True
    },
    {
        "name": "A21: Number of users",
        "sql": "SELECT COUNT(DISTINCT(\"user\".id)) FROM coproduction.public.\"user\"",
        "extract_count": True
    },
    {
        "name": "A22: Average of members per team",
        "sql": "SELECT AVG(MEMBER_COUNT) FROM ( SELECT team_id, COUNT(*) as MEMBER_COUNT FROM  coproduction.public.association_user_team GROUP BY team_id )",
        "extract_count": True
    },
    {
        "name": "A23: Number of success cases publicated",
        "sql": "select COUNT(DISTINCT(id)) from coproduction.public.story",
        "extract_count": True
    },
    {
        "name": "A24: Number of coproduction processes clonated from success cases",
        "sql": "SELECT COUNT(DISTINCT(id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.is_part_of_publication = 'true' AND coproductionprocess.cloned_from_id IS NOT NULL",
        "extract_count": True
    },
    {
        "name": "A25: Number of incentivated processes",
        "sql": "SELECT COUNT(DISTINCT(id)) FROM coproduction.public.coproductionprocess WHERE coproductionprocess.game_id IS NOT NULL",
        "extract_count": True
    },
    {
        "name": "A27: Number of claims",
        "sql": "SELECT COUNT(DISTINCT(coproductionprocessnotification.id)) FROM coproduction.public.coproductionprocessnotification WHERE coproductionprocessnotification.claim_type = 'development'",
        "extract_count": True
    },
    {
        "name": "A29.1: Actions performed over a task: Create task",
        "sql": "SELECT COUNT(action) FROM elastic2.logs.log WHERE model='TASK' AND action='CREATE'",
        "extract_count": True,
    },
    {
        "name": "A29.2: Actions performed over a task: Delete task",
        "sql": "SELECT COUNT(action) FROM elastic2.logs.log WHERE model='TASK' AND action='DISABLE' OR action='DELETE'",
        "extract_count": True,
    },
    {
        "name": "A29.3: Actions performed over a task: Update task",
        "sql": "SELECT COUNT(action) FROM elastic2.logs.log WHERE model='TASK' AND action='UPDATE'",
        "extract_count": True,
    },
    {
        "name": "A30.1: Actions performed over a resource: Create resource",
        "sql": "SELECT COUNT(*) FROM elastic2.logs.log WHERE model='ASSET' AND action='CREATE'",
        "extract_count": True,
    },
    {
        "name": "A30.2: Actions performed over a resource: Delete resource",
        "sql": "SELECT COUNT(*) FROM elastic2.logs.log WHERE model='ASSET' AND action='DELETE'",
        "extract_count": True,
    },
    {
        "name": "A30.3: Actions performed over a resource: Get resource",
        "sql": "SELECT COUNT(*) FROM elastic2.logs.log WHERE model='ASSET' AND action='GET'",
        "extract_count": True,
    },
    {
        "name": "A30.4: Actions performed over a resource: Claim resource",
        "sql": "Select COUNT(*) from coproduction.public.coproductionprocessnotification WHERE coproductionprocessnotification.claim_type = 'development'",
        "extract_count": True,
    },
    {
        "name": "A31: Objectives finished",
        "sql": "SELECT COUNT(*) FROM coproduction.public.objective WHERE progress = 100",
        "extract_count": True,
    },
    {
        "name": "A32: Tasks created",
        "sql": "SELECT COUNT(*) FROM coproduction.public.task",
        "extract_count": True,
    },
    {
        "name": "A33: Percentage of projects conlcuded",
        "sql": "SELECT (finished_coprods*1.0/all_coprods*1.0)*100 from (SELECT COUNT(*) as finished_coprods FROM coproduction.public.coproductionprocess WHERE status='finished'), (SELECT COUNT(*) as all_coprods FROM coproduction.public.coproductionprocess)",
        "extract_count": True,
    },
    {
        "name": "A33.1: Projects concluded",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE status='finished'",
        "extract_count": True,
    },
    {
        "name": "A33.2: Projects in progress",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE status='in_progress'",
        "extract_count": True,
    },
    {
        "name": "A34.1: Resources created by in-progress coprods",
        "sql": "SELECT COUNT(DISTINCT(asset.id)) from coproduction.public.coproductionprocess AS copro INNER JOIN coproduction.public.asset AS asset ON copro.id = asset.coproductionprocess_id WHERE copro.status = 'in_progress'",
        "extract_count": True,
    },
    {
        "name": "A34.2: Resources created by concluded coprods",
        "sql": "SELECT COUNT(DISTINCT(asset.id)) from coproduction.public.coproductionprocess AS copro INNER JOIN coproduction.public.asset AS asset ON copro.id = asset.coproductionprocess_id WHERE copro.status = 'finished'",
        "extract_count": True,
    },
    {
        "name": "A35.1: Creation of phases/objectives/tasks",
        "sql": "SELECT COUNT(*) FROM elastic2.logs.log WHERE action='CREATE' AND (model='PHASE' or model='OBJECTIVE' or model='TASK')",
        "extract_count": True,
    },
    {
        "name": "A35.2: Deletion of phases/objectives/tasks",
        "sql": "SELECT COUNT(*) FROM elastic2.logs.log WHERE (action='DELETE' or action='DISABLE') AND (model='PHASE' or model='OBJECTIVE' or model='TASK')",
        "extract_count": True,
    },
    {
        "name": "A36.1: Projects with modification",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE id NOT IN (SELECT DISTINCT(coproductionprocess_id) FROM elastic2.logs.log WHERE ((action='DELETE' or action='DISABLE' or action='CREATE') AND (model='PHASE' or model='OBJECTIVE' or model='TASk')))",
        "extract_count": True,
    },
    {
        "name": "A36.2: Projects without modification",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocess WHERE id IN (SELECT DISTINCT(coproductionprocess_id) FROM elastic2.logs.log WHERE ((action='DELETE' or action='DISABLE' or action='CREATE') AND (model='PHASE' or model='OBJECTIVE' or model='TASk')))",
        "extract_count": True,
    },
    {
        "name": "A38.1: Amount of knowledge resources created from template",
        "sql": "SELECT COUNT(*) FROM coproduction.public.internalasset WHERe internalasset.knowledgeinterlinker_id IS NOT NULL",
        "extract_count": True,
    },
    {
        "name": "A40.1:	Functionality by type of user (ADMIN): Create",
        "sql": "SELECT COUNT(*) FROM (SELECT CAST(convert_from(convert_to(roles, 'JSON'), 'UTF8') as VARCHAR) roles_text FROM elastic2.logs.log WHERE roles_text LIKE '%administrator%' AND log.action='CREATE')",
        "extract_count": True,
    },
    {
        "name": "A40.2:	Functionality by type of user (ADMIN): Delete",
        "sql": "SELECT COUNT(*) FROM (SELECT CAST(convert_from(convert_to(roles, 'JSON'), 'UTF8') as VARCHAR) roles_text FROM elastic2.logs.log WHERE roles_text LIKE '%administrator%' AND log.action='DELETE')",
        "extract_count": True,
    },
    {
        "name": "A40.3:	Functionality by type of user (ADMIN): Get",
        "sql": "SELECT COUNT(*) FROM (SELECT CAST(convert_from(convert_to(roles, 'JSON'), 'UTF8') as VARCHAR) roles_text FROM elastic2.logs.log WHERE log.action='GET')",
        "extract_count": True,
    },
    {
        "name": "A40.4:	Functionality by type of user (ADMIN): Claim",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocessnotification AS claims INNER JOIN coproduction.public.coproductionprocess_administrators AS admins ON claims.user_id = admins.user_id AND claims.coproductionprocess_id = admins.coproductionprocess_id AND claim_type = 'development'",
        "extract_count": True,
    },
    {
        "name": "A40.5:	Functionality by type of user (ALL): Create",
        "sql": "SELECT COUNT(*) FROM (SELECT CAST(convert_from(convert_to(roles, 'JSON'), 'UTF8') as VARCHAR) roles_text FROM elastic2.logs.log WHERE log.action='CREATE')",
        "extract_count": True,
    },
    {
        "name": "A40.6:	Functionality by type of user (ALL): Delete",
        "sql": "SELECT COUNT(*) FROM (SELECT CAST(convert_from(convert_to(roles, 'JSON'), 'UTF8') as VARCHAR) roles_text FROM elastic2.logs.log WHERE log.action='DELETE')",
        "extract_count": True,
    },
    {
        "name": "A40.7:	Functionality by type of user (ALL): Get",
        "sql": "SELECT COUNT(*) FROM (SELECT CAST(convert_from(convert_to(roles, 'JSON'), 'UTF8') as VARCHAR) roles_text FROM elastic2.logs.log WHERE log.action='GET')",
        "extract_count": True,
    },
    {
        "name": "A40.8:	Functionality by type of user (ALL): Claim",
        "sql": "SELECT COUNT(*) FROM coproduction.public.coproductionprocessnotification AS claims WHERE claim_type = 'development'",
        "extract_count": True,
    }
]

print("Obtaining kpis on", str_date)
results = run_queries(queries)

# print(json.dumps(results))

ENVIRONMENT = os.environ.get("PLATFORM_STACK_NAME")

# send data to GoogleDrive
try:
    result = service.spreadsheets().values().get( spreadsheetId=sheet_id, range=f"{ENVIRONMENT}!A1:ZZ1").execute()
    header = result.get('values', [[]])[0]
except:
    header = []

values_to_insert = []
update = False

if len(header) > 0:
    # check if all query names are present in header and add a new one if not present
    for query in queries:
        name = query.get("name")
        if not name in header:
            header.append(name)
            update = True
            print(f"Added {name} to header")

    # update header if needed
    if update:
        service.spreadsheets().values().update(
            spreadsheetId=sheet_id,
            range=f"{ENVIRONMENT}!A1:ZZ1",
            body={
                "majorDimension": "ROWS",
                "values": [header]
            },
            valueInputOption="USER_ENTERED"
        ).execute()
else:
    # if there are no cells in the header, create them with the kpis names
    header = ["Date time"] + [i.get("name") for i in queries]
    values_to_insert.append(
        header
    )
    values_to_insert.append(
        ["Last value"] + [f"=INDICE( FILTER( {char}3:{char} , NO( ESBLANCO( {char}3:{char} ) ) ) , FILAS( FILTER( {char}3:{char} , NO( ESBLANCO( {char}3:{char} ) ) ) ) )" for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    )

# set each value of row depending on the index of the name of the kpi in the header
row = [str_date]
for query_name, query_result in results.items():
    index = header.index(query_name)
    set_list(row, index, json.dumps(query_result))

values_to_insert.append(
    row
)


# append (the header if necessary) and the row to the existing sheet, defined by ENVIRONMENT (development, demo, zgz...)
service.spreadsheets().values().append(
    spreadsheetId=sheet_id,
    range=f"{ENVIRONMENT}!A:Z",
    body={
        "majorDimension": "ROWS",
        "values": values_to_insert
    },
    valueInputOption="USER_ENTERED"
).execute()

print(
    f"Document updated. See it at: https://docs.google.com/spreadsheets/d/{sheet_id}")
