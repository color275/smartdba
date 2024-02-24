# Generated by Django 2.1.5 on 2020-05-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0187_tuninglist_id_projectlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekDBA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dba', models.CharField(blank=True, choices=[('0', '이치호'), ('1', '이정아'), ('2', '정관호')], default='0', max_length=30, null=True, verbose_name='DBA')),
            ],
            options={
                'verbose_name': '금주DBA',
                'verbose_name_plural': '금주DBA',
                'db_table': 'cust_week_dba',
            },
        ),
        migrations.AlterModelOptions(
            name='batchlist',
            options={'verbose_name': 'SmartDBA배치', 'verbose_name_plural': 'SmartDBA배치'},
        ),
        migrations.AlterModelOptions(
            name='channel',
            options={'verbose_name': '채널구분 (기간계/정보계/MCPC)', 'verbose_name_plural': '채널구분 (기간계/정보계/MCPC)'},
        ),
        migrations.AlterModelOptions(
            name='columnlist',
            options={'verbose_name': 'Column 리스트', 'verbose_name_plural': 'Column 리스트'},
        ),
        migrations.AlterModelOptions(
            name='databasemap',
            options={'verbose_name': '데이터베이스 지도 이미지 매핑 테이블', 'verbose_name_plural': '데이터베이스 지도 이미지 매핑 테이블'},
        ),
        migrations.AlterModelOptions(
            name='datalist',
            options={'verbose_name': '데이터 리스트', 'verbose_name_plural': '데이터 리스트'},
        ),
        migrations.AlterModelOptions(
            name='datarequest',
            options={'verbose_name': '데이터 요청', 'verbose_name_plural': '데이터 요청'},
        ),
        migrations.AlterModelOptions(
            name='datatype',
            options={'verbose_name': '데이터유형구분 (real/staging...)', 'verbose_name_plural': '데이터유형구분 (real/staging...)'},
        ),
        migrations.AlterModelOptions(
            name='dbdetail',
            options={'verbose_name': 'Database 하위 레벨 리스트', 'verbose_name_plural': 'Database 하위 레벨 리스트'},
        ),
        migrations.AlterModelOptions(
            name='dblist',
            options={'ordering': ['db_use'], 'verbose_name': 'Database 상위 레벨 리스트', 'verbose_name_plural': 'Database 상위 레벨 리스트'},
        ),
        migrations.AlterModelOptions(
            name='dbowner',
            options={'verbose_name': 'DB Owner명', 'verbose_name_plural': 'DB Owner명'},
        ),
        migrations.AlterModelOptions(
            name='dbposition',
            options={'verbose_name': 'DBMS 위치', 'verbose_name_plural': 'DBMS 위치'},
        ),
        migrations.AlterModelOptions(
            name='dbtablespace',
            options={'verbose_name': 'DB TBS명', 'verbose_name_plural': 'DB TBS명'},
        ),
        migrations.AlterModelOptions(
            name='dbtype',
            options={'verbose_name': 'DBMS 종류', 'verbose_name_plural': 'DBMS 종류'},
        ),
        migrations.AlterModelOptions(
            name='domain',
            options={'verbose_name': '도메인구분 (고객/상품/주문....)', 'verbose_name_plural': '도메인구분 (고객/상품/주문....)'},
        ),
        migrations.AlterModelOptions(
            name='domainanddblist',
            options={'verbose_name': '도메인-데이터베이스 매핑', 'verbose_name_plural': '도메인-데이터베이스 매핑'},
        ),
        migrations.AlterModelOptions(
            name='grantlist',
            options={'verbose_name': '권한 리스트', 'verbose_name_plural': '권한 리스트'},
        ),
        migrations.AlterModelOptions(
            name='menulist',
            options={'verbose_name': '메뉴분류', 'verbose_name_plural': '메뉴분류'},
        ),
        migrations.AlterModelOptions(
            name='menupermission',
            options={'verbose_name': '메뉴사용자권한', 'verbose_name_plural': '메뉴사용자권한'},
        ),
        migrations.AlterModelOptions(
            name='metagrantdetail',
            options={'verbose_name': '변경관리 권한 상세', 'verbose_name_plural': '변경관리 권한 상세'},
        ),
        migrations.AlterModelOptions(
            name='metagrantlist',
            options={'verbose_name': '변경관리 권한 리스트', 'verbose_name_plural': '변경관리 권한 리스트'},
        ),
        migrations.AlterModelOptions(
            name='metareq',
            options={'verbose_name': '메타변경요청', 'verbose_name_plural': '메타변경요청'},
        ),
        migrations.AlterModelOptions(
            name='metareqlist',
            options={'verbose_name': '메타변경요청상세', 'verbose_name_plural': '메타변경요청상세'},
        ),
        migrations.AlterModelOptions(
            name='objectlist',
            options={'verbose_name': 'Object 리스트', 'verbose_name_plural': 'Object 리스트'},
        ),
        migrations.AlterModelOptions(
            name='opercd',
            options={'verbose_name': '운영구분 (운영/개발/....)', 'verbose_name_plural': '운영구분 (운영/개발/....)'},
        ),
        migrations.AlterModelOptions(
            name='processlist',
            options={'verbose_name': '고객 행동 프로세스 (앱실행/주문완료...)', 'verbose_name_plural': '고객 행동 프로세스 (앱실행/주문완료...)'},
        ),
        migrations.AlterModelOptions(
            name='projectlist',
            options={'verbose_name': '프로젝트 리스트', 'verbose_name_plural': '프로젝트 리스트'},
        ),
        migrations.AlterModelOptions(
            name='sabundbusermapping',
            options={'verbose_name': 'DB USER 매핑', 'verbose_name_plural': 'DB USER 매핑'},
        ),
        migrations.AlterModelOptions(
            name='stddomain',
            options={'verbose_name': '표준도메인', 'verbose_name_plural': '표준도메인'},
        ),
        migrations.AlterModelOptions(
            name='stddomaintype',
            options={'verbose_name': '도메인타입', 'verbose_name_plural': '도메인타입'},
        ),
        migrations.AlterModelOptions(
            name='stdword',
            options={'verbose_name': '표준단어', 'verbose_name_plural': '표준단어'},
        ),
        migrations.AlterModelOptions(
            name='tablelist',
            options={'verbose_name': 'Table 리스트', 'verbose_name_plural': 'Table 리스트'},
        ),
        migrations.AlterModelOptions(
            name='tuninglist',
            options={'verbose_name': '튜닝요청', 'verbose_name_plural': '튜닝요청'},
        ),
        migrations.AlterModelOptions(
            name='tuningstatus',
            options={'verbose_name': '튜닝진행상태 (튜닝요청/튜닝완료/배포요청 등)', 'verbose_name_plural': '튜닝진행상태 (튜닝요청/튜닝완료/배포요청 등)'},
        ),
        migrations.AlterModelOptions(
            name='userclickdata',
            options={'verbose_name': '사용자 클릭데이터', 'verbose_name_plural': '사용자 클릭데이터'},
        ),
        migrations.AlterModelOptions(
            name='userexecutesql',
            options={'verbose_name': '사용자 실행SQL 이력', 'verbose_name_plural': '사용자 실행SQL 이력'},
        ),
        migrations.AlterModelOptions(
            name='userlist',
            options={'verbose_name': 'User 리스트', 'verbose_name_plural': 'User 리스트'},
        ),
        migrations.AlterModelOptions(
            name='userrequestaccountopenhist',
            options={'verbose_name': '계정활성화신청이력', 'verbose_name_plural': '계정활성화신청이력'},
        ),
        migrations.AlterModelOptions(
            name='userrequestdata',
            options={'verbose_name': '사용자 데이터 요청', 'verbose_name_plural': '사용자 데이터 요청'},
        ),
        migrations.AlterModelOptions(
            name='userrequesttabprivhist',
            options={'verbose_name': '테이블권한신청', 'verbose_name_plural': '테이블권한신청'},
        ),
        migrations.AlterModelOptions(
            name='userrequestword',
            options={'verbose_name': '사용자 데이터 요청', 'verbose_name_plural': '사용자 데이터 요청'},
        ),
        migrations.AlterModelOptions(
            name='usersearchkeyword',
            options={'verbose_name': '사용자 검색키워드', 'verbose_name_plural': '사용자 검색키워드'},
        ),
        migrations.AlterModelOptions(
            name='uservisit',
            options={'verbose_name': '사용자방문이력', 'verbose_name_plural': '사용자방문이력'},
        ),
        migrations.AlterField(
            model_name='metagrantdetail',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='GRANTEE'),
        ),
        migrations.AlterField(
            model_name='userlist',
            name='request_status',
            field=models.CharField(blank=True, choices=[('0', '미신청'), ('1', '신청중')], default='0', max_length=100, null=True, verbose_name='신청상태'),
        ),
    ]
