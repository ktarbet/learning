set ANSI_NULLS ON
set QUOTED_IDENTIFIER ON
go


-- =============================================
-- Author:		<Author,,Karl Tarbet>
-- Create date: <Create January 9, 2005>
-- Description:	<returns a list of recipient financial and progress reports>
-- =============================================
ALTER PROCEDURE [fao].[proc_RecipientReports]
    @ArePastDue as bit,
    @DaysUntilDue as integer
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
declare @sqlCmd as varchar(2048)

set @sqlCmd = 'select ''Progress'' ReportType, a.AgreementNumber,cast(ModificationNumber as varchar(3)) mod, Recipient,OfficeID, '
            + ' cast(ReclamationPOC as varchar(15)) GCAOR, r.DueDate,ProgressReportFrequency as Frequency '
            + 'from fao.view_ActiveAgreements a '
            + ' join fao.tblReportProgress r on  '
            + ' a.AgreementNumber  = r.AgreementNumber '
            +' where (r.Received =0 and r.Waived=0) ';

       if @ArePastDue = 1
            set @sqlCmd = @sqlCmd +'  and DueDate < getdate()  '
      else
           set @sqlCmd = @sqlCmd +' and DueDate > getdate() and DueDate <DATEADD(dd,' + str(@DaysUntilDue) +' , getdate()) '


set @sqlCmd = @sqlCmd + 'UNION select ''Financial'' ReportType, a.AgreementNumber,cast(ModificationNumber as varchar(3)) mod, Recipient,OfficeID, '
            + ' cast(ReclamationPOC as varchar(15)) GCAOR, r.DueDate,FinancialReportFrequency as Frequency '
            + 'from fao.view_ActiveAgreements a '
            + ' join fao.tblReportFinancial r on  '
            + ' a.AgreementNumber  = r.AgreementNumber '
            +' where (r.Received =0 and r.Waived=0) ';

       if @ArePastDue = 1
            set @sqlCmd = @sqlCmd +'  and DueDate < getdate()  '
      else
           set @sqlCmd = @sqlCmd +' and DueDate > getdate() and DueDate <DATEADD(dd,' + str(@DaysUntilDue) +' , getdate()) '
 

set @sqlCmd = @sqlCmd + ' order by ReportType,OfficeID,GCAOR,DueDate '

exec(@sqlCmd)

END


