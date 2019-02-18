
SELECT * FROM sys.configurations
ORDER BY name ;
GO



select @@version
Use Master
GO
Select owning_principle_name, instance_pipe_name from sys.dm_child_instances
GO
