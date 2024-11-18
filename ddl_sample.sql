create table dbo.Example
(
    tpid                        int identity(100, 1)    primary key,
    orgid                       int                    not null,
    name                        varchar(50)            not null,
    address1                    varchar(100)           null,
    email                       nvarchar(255)          unique,
    status                      char(1)                default 'A',
    created_date                datetime               default getdate(),
    annual_revenue              decimal(12,2)          default 0.00,
    is_active                   bit                    default 1,
    contact_phone               varchar(20)            null,
    description                 ntext                  null,
    last_updated                timestamp
)
